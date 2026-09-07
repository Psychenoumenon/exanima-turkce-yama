# -*- coding: utf-8 -*-
"""Guc agaci (.pwr) metinlerinin Turkce karsiliklari.

TERIMLER (exe cevirisiyle birebir ayni tutuldu):
    binding -> bag            Inversion   -> Tersine Cevirme
    Union      -> Birlik      Continuity  -> Süreklilik
    Coherence  -> Tutarlilik  Expansion   -> Genisleme
    Convergence-> Odaklanma   Revelation  -> Kesif

USLUP: guc aciklamalari 3. tekil betimleyici ("...saglar."), Turkce oyun
yerellestirmesinde standart olan bicim. Guc ADLARI Basligin Her Kelimesi Buyuk.
"""

N = '\r\n'
NN = '\r\n\r\n'

ADLAR = {
    'Calm': 'Sakinleştirme',
    'Enrage': 'Öfkelendirme',
    'Trust': 'Güven',
    'Fear': 'Korku',
    'Confusion': 'Şaşkınlık',
    'Suspicion': 'Kuşku',
    'Loyalty': 'Sadakat',
    'Embolden': 'Yüreklendirme',
    'Possession': 'Ele Geçirme',
    'Mask Mind': 'Zihin Gizleme',
    'Mind Mask': 'Zihin Maskesi',
    'Sense Minds': 'Zihin Sezme',
    'Mind Sense': 'Zihin Sezgisi',
    'Spirit Form': 'Ruh Bedeni',
    'Command Dead': 'Ölülere Hükmetme',
    'Banish Dead': 'Ölüleri Kovma',
    'Raise Dead': 'Ölüleri Diriltme',
    'Directed Trust': 'Yönlendirilmiş Güven',
    'Mass Calm': 'Toplu Sakinleştirme',
    'Mass Enrage': 'Toplu Öfkelendirme',
    'Mass Fear': 'Toplu Korku',
    'Mass Confusion': 'Toplu Şaşkınlık',
    # --- Kuvvet (Force) ---
    'Wave': 'Dalga',
    'Blast': 'Patlama',
    'Bolt': 'Ok',
    'Barrier': 'Bariyer',
    'Barricade': 'Kuvvet Duvarı',
    'Bubble': 'Küre',
    'Shield': 'Kalkan',
    'Shell': 'Kabuk',
    'Ward': 'Siper',
    'Kinesis': 'Devinim',
    'Strikes': 'Vuruşlar',
    'Torrent': 'Sağanak',
    'Momentum': 'İvme',
    'Retrieve': 'Çekme',
    'Throw': 'Fırlatma',
    'Crush': 'Ezme',
    'Levitate': 'Süzülme',
    # --- Enerji / Yer degistirme ---
    'Shock': 'Şok',
    'Vanish': 'Yok Olma',
}

ACIKLAMALAR = {
    N + 'Requires Inversion.': N + 'Tersine Çevirme gerekir.',
    N + 'Requires Continuity.': N + 'Süreklilik gerekir.',

    'Bubble can be formed around other targets.':
        'Küre, başka hedeflerin çevresinde de oluşturulabilir.',
    'Lift and throw objects towards a desired target.':
        'Nesneleri kaldırıp istediğiniz hedefe fırlatır.',
    'Cause a target to trust you for a short duration.':
        'Bir hedefin kısa süreliğine size güvenmesini sağlar.',
    "Cleanse a target's mind of concerns and aggression.":
        'Bir hedefin zihnini kaygıdan ve saldırganlıktan arındırır.',
    'Charge and release a powerful shock from your hand.':
        'Elinizde güçlü bir şok toplayıp boşaltır.',
    'Unleash a sustained stream of force in front of you.':
        'Önünüze kesintisiz bir kuvvet akımı salar.',
    'Release a blast pushing away anything in front of you.':
        'Önünüzdeki her şeyi savuran bir patlama yayar.',
    'Your physical form enters another plane, becoming intangible.':
        'Bedeniniz başka bir düzleme geçerek elle tutulamaz hâle gelir.',
    'Sense minds in your vicinity and reveal their emotional state.':
        'Yakınınızdaki zihinleri sezer ve duygusal durumlarını açığa çıkarır.',
    'Envelop your body in shaped force, partially absorbing impacts.':
        'Bedeninizi biçimlendirilmiş kuvvetle sarar, darbeleri kısmen soğurur.',
    'Briefly confuse a target and cause them to not recognise others.':
        'Bir hedefi kısa süre şaşkına çevirir; başkalarını tanıyamaz hâle getirir.',

    'Move and manipulate distant objects.' + NN + 'Requires Coherence.':
        'Uzaktaki nesneleri hareket ettirir ve yönlendirir.' + NN + 'Tutarlılık gerekir.',
    'Cause a target to trust another for a time.' + NN + '<UNAVAILABLE>':
        'Bir hedefin bir süre başka birine güvenmesini sağlar.' + NN + '<KULLANILAMAZ>',
    'Enrage multiple targets with a single binding.' + NN + '<UNAVAILABLE>':
        'Tek bir bağla birden çok hedefi öfkelendirir.' + NN + '<KULLANILAMAZ>',
    'Confuse multiple targets with a single binding.' + NN + '<UNAVAILABLE>':
        'Tek bir bağla birden çok hedefi şaşkına çevirir.' + NN + '<KULLANILAMAZ>',
    'Cause fear in multiple targets with one binding.' + NN + '<UNAVAILABLE>':
        'Tek bir bağla birden çok hedefe korku salar.' + NN + '<KULLANILAMAZ>',
    'Instill calm on multiple targets with a single binding.' + NN + '<UNAVAILABLE>':
        'Tek bir bağla birden çok hedefi sakinleştirir.' + NN + '<KULLANILAMAZ>',
    'Continuously sense minds in your vicinity.' + NN + 'Requires Continuity.':
        'Yakınınızdaki zihinleri sürekli olarak sezer.' + NN + 'Süreklilik gerekir.',
    'Provide a target with a great surge in courage.' + NN + 'Requires Inversion.':
        'Bir hedefe büyük bir cesaret dalgası verir.' + NN + 'Tersine Çevirme gerekir.',
    'Conceal your mind, making it difficult to detect.' + NN + 'Requires Inversion.':
        'Zihninizi gizler, sezilmesini güçleştirir.' + NN + 'Tersine Çevirme gerekir.',
    "Take direct control of a target's actions." + NN + 'Requires Union, Continuity.':
        'Bir hedefin eylemlerinin denetimini doğrudan ele alır.' + NN + 'Birlik ve Süreklilik gerekir.',
    'Cause the target to suffer an uncontrollable rage.' + NN + 'Requires Inversion.':
        'Hedefi denetlenemez bir öfkeye sürükler.' + NN + 'Tersine Çevirme gerekir.',
    'Cause a target to be overcome with a feeling of dread.' + NN + 'Requires Union.':
        'Bir hedefi derin bir dehşet duygusuna boğar.' + NN + 'Birlik gerekir.',
    'Empower your strikes to deliver stronger impacts.' + NN + 'Requires Continuity.':
        'Vuruşlarınızı güçlendirir, daha sert darbeler indirmenizi sağlar.' + NN + 'Süreklilik gerekir.',
    'Cause someone to trust you and follow your command.' + NN + 'Requires Continuity.':
        'Birinin size güvenmesini ve buyruğunuza uymasını sağlar.' + NN + 'Süreklilik gerekir.',
    'Quickly form a barrier of dense force to protect you.' + NN + 'Requires Coherence.':
        'Sizi korumak için yoğun kuvvetten hızla bir bariyer oluşturur.' + NN + 'Tutarlılık gerekir.',
    'Damage the link that sustains the dead, eventually severing it.' + NN + '<UNAVAILABLE>':
        'Ölüleri ayakta tutan bağı yıpratır ve sonunda koparır.' + NN + '<KULLANILAMAZ>',
    'Continuously mask your mind from those that would sense it.' + NN + 'Requires Continuity.':
        'Zihninizi, sezmeye çalışanlardan sürekli olarak gizler.' + NN + 'Süreklilik gerekir.',
    'Form a bubble of impenetrable force around yourself.' + NN + 'Requires Union, Continuity.':
        'Çevrenizde aşılamaz kuvvetten bir küre oluşturur.' + NN + 'Birlik ve Süreklilik gerekir.',
    'Render target suspicious of those they would otherwise trust.' + NN + 'Requires Inversion.':
        'Hedefi, normalde güvendiği kişilerden kuşkulanır hâle getirir.' + NN + 'Tersine Çevirme gerekir.',
    'Command the dead to repossess their remains in your service.' + NN + 'Requires Continuity.':
        'Ölülere, hizmetinizde olmak üzere kalıntılarına dönmelerini buyurur.' + NN + 'Süreklilik gerekir.',
    'Focus your mind to leave your body and enter the spirit realm.' + NN + 'Requires Coherence.':
        'Zihninizi toplayıp bedeninizden ayrılır, ruhlar diyarına geçersiniz.' + NN + 'Tutarlılık gerekir.',
    'Release a wave of force pushing away anything surrounding you.' + NN + 'Requires Expansion.':
        'Çevrenizdeki her şeyi savuran bir kuvvet dalgası salar.' + NN + 'Genişleme gerekir.',
    'Release a bolt of focused force able to hit distant targets.' + NN + 'Requires Convergence.':
        'Uzaktaki hedefleri vurabilen, odaklanmış bir kuvvet oku salar.' + NN + 'Odaklanma gerekir.',
    'Call the dead to repossess their remains, but without your binding.' + NN + 'Requires Revelation.':
        'Ölüleri kalıntılarına dönmeye çağırır, ama bağınız olmadan.' + NN + 'Keşif gerekir.',
    'Fully focus your mind to remain in spirit form indefinitely.' + NN + 'Requires Revelation, Continuity.':
        'Zihninizi tümüyle toplayarak süresiz olarak ruh bedeninde kalırsınız.' + NN + 'Keşif ve Süreklilik gerekir.',
    'Create a wall of force that prevents passage in one direction.' + NN + 'Requires Expansion, Continuity.':
        'Tek yönde geçişi engelleyen bir kuvvet duvarı yaratır.' + NN + 'Genişleme ve Süreklilik gerekir.',
}

TR = dict(ADLAR)
TR.update(ACIKLAMALAR)
