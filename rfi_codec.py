"""
Exanima .rfi bitmap format - container + "RFI-RLE" codec.
Reverse engineered from Resource.rpk / *.rfc assets. Verified by byte-exact
re-encoding of all 45 compressed .rfi files found in the game data.

CONTAINER (32-byte header, little endian)
  0x00 u32 magic      = 0x1D2D3DC6   (bytes: c6 3d 2d 1d)
  0x04 u32 width
  0x08 u32 height
  0x0C u32 frames     = 1
  0x10 u32 pixfmt     channel descriptor, see NCHAN below
  0x14 u32 flags      (uv / sampler bits - not needed to decode)
  0x18 u32 storage    0x10000000 = raw (body is the pixels)
                      0x50000000 = RLE compressed (body is an RFI-RLE stream)
  0x1C u32 datasize   exact size of the DECOMPRESSED body, in bytes
  0x20 .. body

  datasize == width*height*nchan            -> no mipmaps
  datasize == mipsum(width,height)*nchan    -> full mipmap chain follows
                                               the base image (each level
                                               halved, down to 1x1)

CODEC  (byte oriented run/literal RLE; no entropy coding, no dictionary)
  Let PX = nchan bytes (one pixel, channel-interleaved).
  Let RUNBASE = 64 if nchan == 1 else 63.

  loop until the stream is consumed:
      c = next byte
      if c <  RUNBASE:   LITERAL - copy the next (c + 1) pixels verbatim
      else:              RUN     - read 1 pixel, emit it (c - 61) times

  So run lengths are (RUNBASE-61) .. 194 and literal lengths are 1 .. RUNBASE.
  RUNBASE is placed exactly at the shortest *profitable* run: for 1 byte/px a
  2-pixel run costs the same as a literal (2 bytes) so the minimum run is 3;
  for >=2 bytes/px a 2-pixel run already saves bytes, so the minimum run is 2.
  The opcode space is partitioned exactly: RUNBASE literal codes + (256-RUNBASE)
  run codes = 256.

ROW ORDER is BOTTOM-UP: the first decoded row is the bottom row of the image.
"""
import struct

MAGIC   = 0x1D2D3DC6
RAW     = 0x10000000
RLE     = 0x50000000
RUN_MAX = 194
BIAS    = 61

# pixel-format word (header +0x10) -> bytes per pixel
NCHAN = {
    0x01002008: 1,   # A8 / L8   (fontbase24r, guiskin, cursors, skillicon, ...)
    0x01004200: 1,   # L8        (pwrsframes, wndbkg02)
    0x01006208: 2,   # L8A8      (titlefont, dotrating, sgsklicons)
    0x0100c600: 3,   # R8G8B8    (thm*ico*)
    0x0100e608: 4,   # R8G8B8A8  (coinicons, maintitle01, tut*, seasonrwrd*)
}


def runbase(nchan):
    return 64 if nchan == 1 else 63


def rle_decode(body, nchan=1, expected=None):
    """Decompress an RFI-RLE stream. Returns bytes."""
    rb = runbase(nchan)
    out = bytearray()
    i, n = 0, len(body)
    if nchan == 1:                                   # fast path
        while i < n:
            c = body[i]; i += 1
            if c < rb:
                k = c + 1
                out += body[i:i + k]; i += k
            else:
                out += bytes([body[i]]) * (c - BIAS); i += 1
    else:
        while i < n:
            c = body[i]; i += 1
            if c < rb:
                k = (c + 1) * nchan
                out += body[i:i + k]; i += k
            else:
                out += body[i:i + nchan] * (c - BIAS); i += nchan
    if expected is not None and len(out) != expected:
        raise ValueError("decoded %d bytes, header says %d" % (len(out), expected))
    return bytes(out)


def rle_encode(data, nchan=1):
    """Compress to an RFI-RLE stream. Reproduces Bare Mettle's output byte-exactly."""
    rb = runbase(nchan)
    minrun = rb - BIAS                                # 3 for 1ch, 2 otherwise
    out = bytearray()
    npx = len(data) // nchan
    lit = []            # pending literal pixels (as memoryview slices)
    i = 0

    def flush():
        while lit:
            k = min(len(lit), rb)
            out.append(k - 1)
            for p in lit[:k]:
                out.extend(p)
            del lit[:k]

    while i < npx:
        a = i * nchan
        v = data[a:a + nchan]
        j = i + 1
        while j < npx and j - i < RUN_MAX and data[j * nchan:(j + 1) * nchan] == v:
            j += 1
        rl = j - i
        if rl >= minrun:
            flush()
            out.append(rl + BIAS)
            out.extend(v)
            i = j
        else:
            lit.append(v)
            i += 1
            if len(lit) == rb:
                flush()
    flush()
    return bytes(out)


def mipsum(w, h):
    """Total pixels of a full mip chain starting at w x h (down to 1x1)."""
    t = 0
    while True:
        t += w * h
        if w == 1 and h == 1:
            break
        w = max(1, w >> 1); h = max(1, h >> 1)
    return t


def read_rfi(path):
    d = open(path, 'rb').read()
    h = list(struct.unpack('<8I', d[:32]))
    if h[0] != MAGIC:
        raise ValueError("not an .rfi file")
    w, ht, fmt = h[1], h[2], h[4]
    nchan = NCHAN.get(fmt)
    if nchan is None:
        raise ValueError("unknown pixel format 0x%08x" % fmt)
    body = d[32:]
    data = body if h[6] == RAW else rle_decode(body, nchan, h[7])
    stride = w * nchan
    base = data[:stride * ht]
    rows = [base[y * stride:(y + 1) * stride] for y in range(ht)]
    return dict(width=w, height=ht, nchan=nchan, header=h,
                compressed=(h[6] == RLE),
                has_mips=(h[7] == mipsum(w, ht) * nchan),
                pixels=b"".join(reversed(rows)),      # top-down
                mips=data[stride * ht:],
                data=data)


def write_rfi(path, width, height, pixels_topdown, nchan=1, header=None,
              mips=b"", compress=True):
    """Write an .rfi. pixels_topdown = width*height*nchan bytes, top row first."""
    stride = width * nchan
    assert len(pixels_topdown) == stride * height
    rows = [pixels_topdown[y * stride:(y + 1) * stride] for y in range(height)]
    data = b"".join(reversed(rows)) + mips             # store bottom-up
    fmt = {1: 0x01002008, 2: 0x01006208, 3: 0x0100c600, 4: 0x0100e608}[nchan]
    h = list(header) if header else [MAGIC, width, height, 1, fmt, 0x20200000, RLE, 0]
    h[0], h[1], h[2], h[4] = MAGIC, width, height, h[4] if header else fmt
    if compress:
        body = rle_encode(data, nchan); h[6] = RLE
    else:
        body = data; h[6] = RAW
    h[7] = len(data)
    open(path, 'wb').write(struct.pack('<8I', *h) + body)
    return len(body)
