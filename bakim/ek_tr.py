# -*- coding: utf-8 -*-
"""Eski tarayicinin kacirdigi exe metinleri.

Bu metinler CP1252 '…' (0x85) ya da bare-CR icerdigi ve/veya 200 bayttan uzun
oldugu icin ilk regex'e takilmamisti: karakter secim ekrani aciklamalari, arena
mac tanimlari ve arena ussu ogreticileri.

USLUP KURALI
  Anlati metni (karakter gecmisi)  -> 2. tekil "sen"  (surukleyici)
  Arayuz talimati (arena ogretici) -> 2. cogul "siz"  (exe'nin geri kalaniyla ayni)

TERIMLER exe cevirisiyle birebir: Match=Mac, Company=Boluk, Roster=Kadro,
Manage=Yonet, Arsenal=Cephane, Recruit=Kirala, Hire=Tut, Rank=Rutbe,
Tier=Kademe, Loadout=Techizat, Tournament=Turnuva, Prize=Odul.

Anahtarlar exe'deki bayt dizisiyle BIREBIR ayni olmali; degerler CP1254'e
kodlanabilmeli ve align8(uzunluk+1)-1 tamponuna sigmalidir (kontrol: ek_kontrol.py).
"""

CR = '\r'
CR2 = '\r\r'
CRLF = '\r\n'

TR = {
    # ---------------- ogretici ----------------
    'Hold [tcol=FFE399]Powers[/tcol] to access the power tree.' + CR2 +
    'Press [tcol=FFE399]Use Power[/tcol] with the power bar open to use a power '
    'directly without changing which is active.' + CR2 +
    'You can toggle in and out of dialogue mode without ending the conversation '
    'by pressing [tcol=FFE399]Talk[/tcol].':
        'Güç ağacını açmak için [tcol=FFE399]Güçler[/tcol] tuşunu basılı tutun.' + CR2 +
        'Güç çubuğu açıkken [tcol=FFE399]Güç kullan[/tcol] tuşuna basarsanız etkin '
        'gücü değiştirmeden doğrudan bir güç kullanırsınız.' + CR2 +
        '[tcol=FFE399]Konuş[/tcol] tuşuyla konuşmayı bitirmeden diyalog kipine '
        'girip çıkabilirsiniz.',

    'Analysing system…': 'Sistem inceleniyor…',

    # Son taramada yakalanan, ilk turda cevrilmemis kalan oyuncu metinleri
    'This system does not meet the minimum requirements to run Exanima. Updating the graphics driver may solve the problem.':
        'Bu sistem Exanima\'nın en düşük gereksinimlerini karşılamıyor. Ekran kartı sürücüsünü güncellemek sorunu çözebilir.',
    'Merchants provide an inventory of items for you to buy. They can help you find more specific items by providing stock of a particular type and rank.':
        'Tüccarlar satın alabileceğiniz eşyalar sunar. Belirli tür ve rütbede stok getirerek aradığınız eşyaları bulmanıza yardım edebilirler.',
    "Physicians improve the rate of healing of your fighters and can save fighters from death if the injuries sustained aren't too severe.":
        'Hekimler dövüşçülerinizin iyileşme hızını artırır; yaralar çok ağır değilse dövüşçüleri ölümden kurtarabilirler.',
    'Trainers increase the rate at which your fighters learn skills. They can also teach the techniques they know to your fighters when they are idle.':
        'Eğitmenler dövüşçülerinizin yetenek öğrenme hızını artırır. Boştayken bildikleri teknikleri dövüşçülerinize öğretebilirler.',
    'TO BE CONTINUED…': 'DEVAMI GELECEK…',

    # ---------------- karakter secimi ----------------
    "You don't know who you are, but there may be great potential in you…":
        'Kim olduğunu bilmiyorsun, ama içinde büyük bir güç yatıyor olabilir…',

    "You have limited combat experience, but thanks to your family's wealth you "
    "were able to train, purchase the equipment and become knighted. Your lord "
    "Ermus has tasked you to investigate a series of disappearances in the "
    "villages of Benston and Pirn within his tenure. The trail has led you here…":
        'Savaş deneyimin sınırlı, ama ailenin varlığı sayesinde eğitim alıp '
        'teçhizatını edinebildin ve şövalye ilan edildin. Efendin Ermus, '
        'topraklarındaki Benston ve Pirn köylerinde yaşanan bir dizi kayboluşu '
        'araştırmanı buyurdu. İzler seni buraya getirdi…',

    "You are sworn to uphold the law of Ardent and you carry the king's authority "
    "over all. The king has been petitioned to stop a series of abductions "
    "occuring in the villages of Benston and Pirn. A proctor was sent before you, "
    "but she has not reported back and is considered missing.":
        'Ardent yasasını korumaya ant içtin ve her şeyin üstünde kralın yetkisini '
        'taşıyorsun. Krala, Benston ve Pirn köylerinde süregelen bir dizi kaçırma '
        'olayını durdurması için dilekçe verildi. Senden önce bir vekil yollandı, '
        'ama haber vermedi ve kayıp sayılıyor.',

    'You are a cobbler of notable skill from the village of Pirn. From time to '
    'time you travel to nearby villages in an effort to expand your market. On '
    'the latest such occasion you were ambushed during your trip. Your assailants '
    'appear to have no interest in your goods, they abducted you without giving '
    'reason.':
        'Pirn köyünden, işinin ehli bir ayakkabıcısın. Zaman zaman pazarını '
        'genişletmek için yakın köylere yol alırsın. Bu son yolculuğunda pusuya '
        'düşürüldün. Sana saldıranlar malınla hiç ilgilenmedi; hiçbir gerekçe '
        'göstermeden seni kaçırdılar.',

    # ---------------- arena mac tanimlari ----------------
    '[algn=2]Six fighters engage in unarmed combat until only one stands.' + CRLF +
    'Winners are chosen based on their performance.':
        '[algn=2]Altı dövüşçü, tek kişi ayakta kalana dek silahsız dövüşür.' + CRLF +
        'Kazananlar gösterdikleri başarıya göre seçilir.',

    '[algn=2]Six fighters engage in combat until only one remains standing.' + CRLF +
    'Winners are chosen based on their performance.':
        '[algn=2]Altı dövüşçü, tek kişi ayakta kalana dek dövüşür.' + CRLF +
        'Kazananlar gösterdikleri başarıya göre seçilir.',

    '[algn=2]Three fighters per side duel until one team has no more reserves.' + CRLF +
    'Each round lost reduces the prize.':
        '[algn=2]Üç kişilik takımlar, birinin yedeği bitene dek düello yapar.' + CRLF +
        'Kaybedilen her raunt ödülü azaltır.',

    '[algn=2]Four rounds of duels using a weapon chosen for the event.' + CRLF +
    'Victors face each other until one remains.':
        '[algn=2]Etkinlik için seçilen bir silahla dört raunt düello yapılır.' + CRLF +
        'Galipler, tek kişi kalana dek karşılaşır.',

    '[algn=2]Six fighters engage in combat using a weapon chosen for the event.' + CRLF +
    'Winners are chosen based on their performance.':
        '[algn=2]Altı dövüşçü, etkinlik için seçilen bir silahla dövüşür.' + CRLF +
        'Kazananlar gösterdikleri başarıya göre seçilir.',

    '[algn=2]Teams of two face each other in three rounds. ' + CRLF +
    'Defeated fighters do not continue to the next round.':
        '[algn=2]İkişer kişilik takımlar üç raunt karşı karşıya gelir.' + CRLF +
        'Yenilen dövüşçüler sonraki raunda geçemez.',

    '[algn=2]There are no more matches running this day.' + CRLF +
    'End the day to participate in more matches.':
        '[algn=2]Bugün için başka maç kalmadı.' + CRLF +
        'Daha fazla maça katılmak için günü bitirin.',

    # ---------------- arena ussu ogreticileri ----------------
    CR + 'This is your base of operations and living space.' + CR2 +
    '[tcol=FFE399]Manage[/tcol] your company by clicking on the board on our left.' + CR2 +
    'Directly ahead is a [tcol=FFE399]Shop[/tcol] where you can buy and sell equipment.' + CR2 +
    '[tcol=FFE399]Matches[/tcol] that you can participate in are accessed from the '
    'board on your right.':
        CR + 'Burası hem üssünüz hem de yaşam alanınız.' + CR2 +
        'Solunuzdaki panoya tıklayarak bölüğünüzü [tcol=FFE399]yönetin[/tcol].' + CR2 +
        'Tam karşınızda teçhizat alıp satabileceğiniz bir [tcol=FFE399]Dükkân[/tcol] var.' + CR2 +
        'Katılabileceğiniz [tcol=FFE399]Maçlar[/tcol] sağınızdaki panodan açılır.',

    'The inventory shows items you are currently wearing and carrying.' + CR2 +
    'Items you wear while outside of a match are not carried into matches. To equip '
    'items for combat you must use the management screen.':
        'Envanter, üzerinizdeki ve taşıdığınız eşyaları gösterir.' + CR2 +
        'Maç dışında giydikleriniz maça taşınmaz. Dövüş için teçhizat kuşanmak '
        'isterseniz yönetim ekranını kullanmalısınız.',

    'Matches are split into three main categories.' + CR2 +
    '[tcol=FFE399]Standard[/tcol] matches can be run at any time and configured to '
    'your preference.' + CR2 +
    '[tcol=FFEF99]Specials[/tcol] change daily and can only be run when and as '
    'available.' + CR2 +
    '[tcol=FFE399]Tournaments[/tcol] are weekly multiple match events where fighting '
    'companies compete for important prizes.' + CR2 +
    'Select a match and then enter your fighters by dragging them to the right. Some '
    'matches require multiple participants.' + CR2 +
    '[tcol=FFE399]Rank[/tcol] is a requirement, your fighter must attain this rank '
    'before they can participate.' + CR2 +
    '[tcol=FFE399]Tier[/tcol] indicates the level of equipment used in the match. '
    'This corresponds to your loadouts in the manage screen.':
        'Maçlar üç ana türe ayrılır.' + CR2 +
        '[tcol=FFE399]Standart[/tcol] maçlar her an düzenlenebilir ve dilediğiniz '
        'gibi ayarlanabilir.' + CR2 +
        '[tcol=FFEF99]Özel[/tcol] maçlar her gün değişir; yalnızca açık oldukları '
        'zaman oynanabilir.' + CR2 +
        '[tcol=FFE399]Turnuvalar[/tcol] haftalıktır; dövüş bölüklerinin önemli '
        'ödüller için yarıştığı çok maçlı etkinliklerdir.' + CR2 +
        'Bir maç seçin, sonra dövüşçülerinizi sağa sürükleyerek kaydedin. Bazı '
        'maçlar birden çok katılımcı ister.' + CR2 +
        '[tcol=FFE399]Rütbe[/tcol] bir koşuldur; dövüşçünüz katılabilmek için o '
        'rütbeye ulaşmalıdır.' + CR2 +
        '[tcol=FFE399]Kademe[/tcol] maçta kullanılan teçhizatın düzeyini gösterir. '
        'Bu, yönetim ekranındaki teçhizatlarınıza karşılık gelir.',

    'This is where you can buy and sell items.' + CR2 +
    "Drag items you want to buy from the shop's stock to the right pane, items you "
    'want to sell go in the left pane.' + CR2 +
    'You can try items on before you buy them by dragging them on to the paperdoll.' + CR2 +
    'Note that rank restrictions are applied to some items. You must achieve that '
    'rank and participate in appropriate matches to use these.' + CR2 +
    'Invest early and invest wisely, even a few basic layers of clothing can offer '
    'great protection from injury.':
        'Burada eşya alıp satabilirsiniz.' + CR2 +
        'Almak istediklerinizi dükkânın stokundan sağ bölmeye, satmak '
        'istediklerinizi sol bölmeye sürükleyin.' + CR2 +
        'Almadan önce eşyaları mankene sürükleyerek deneyebilirsiniz.' + CR2 +
        'Bazı eşyalarda rütbe koşulu vardır. Bunları kullanmak için o rütbeye '
        'ulaşmalı ve uygun maçlara katılmalısınız.' + CR2 +
        'Erken ve akıllıca yatırım yapın; birkaç kat basit giysi bile '
        'yaralanmaya karşı iyi koruma sağlar.',

    '[tcol=FFE399]Manage[/tcol] equipment and training for your roster.' + CR2 +
    'The [tcol=FFE399]Arsenal[/tcol] allows you to organise your equipment.' + CR2 +
    '[tcol=FFE399]Recruit[/tcol] new fighters to control in battle.' + CR2 +
    '[tcol=FFE399]Hire[/tcol] combatants for team matches and other staff.' + CR2 +
    'Daily [tcol=FFE399]report[/tcol] items can be double clicked to take action.':
        'Kadronuzun teçhizatını ve eğitimini [tcol=FFE399]yönetin[/tcol].' + CR2 +
        '[tcol=FFE399]Cephane[/tcol] teçhizatınızı düzenlemenizi sağlar.' + CR2 +
        'Dövüşte yöneteceğiniz yeni dövüşçüleri [tcol=FFE399]kiralayın[/tcol].' + CR2 +
        'Takım maçları için savaşçıları ve diğer görevlileri [tcol=FFE399]tutun[/tcol].' + CR2 +
        'Günlük [tcol=FFE399]rapor[/tcol] satırlarına çift tıklayıp işlem yapın.',

    'Fighters gain a [tcol=FFE399]rank[/tcol] every two skill techniques learnt.' + CR2 +
    'Each rank has a corresponding loadout. Which loadout is used depends on the tier '
    'of the match. Use the slider to select a ranked loadout.' + CR2 +
    '[tcol=FFE399]Point[/tcol] limits are also applied to each rank. Every item carries '
    'a point cost.':
        'Dövüşçüler öğrendikleri her iki teknikte bir [tcol=FFE399]rütbe[/tcol] kazanır.' + CR2 +
        'Her rütbenin bir teçhizatı vardır. Hangisinin kullanılacağı maçın kademesine '
        'bağlıdır. Rütbeli teçhizatı sürgüyle seçin.' + CR2 +
        'Her rütbeye ayrıca [tcol=FFE399]puan[/tcol] sınırı uygulanır. Her eşyanın bir '
        'puan bedeli vardır.',

    '[tcol=FF0000C0]You are about to enter your manager into a match. If your manager '
    'is killed you will lose all progress![/tcol]' + CR2 +
    'Consider recruiting fighters to avoid unnecessary risks.':
        '[tcol=FF0000C0]Yöneticinizi bir maça sokmak üzeresiniz. Yöneticiniz ölürse tüm '
        'ilerlemenizi yitirirsiniz![/tcol]' + CR2 +
        'Gereksiz riske girmemek için dövüşçü kiralamayı düşünün.',

    'The items you have purchased can be found in your Arsenal, accessible through '
    'the Roster.':
        'Satın aldığınız eşyalar, Kadro üzerinden açılan Cephane bölümündedir.',

    'Tournaments are held weekly. Fighting companies compete in each tournament for a '
    'prize. If a company wins all four tournaments in a season they are awarded an '
    'exclusive suit of armour.' + CR2 +
    'You must enter fighters in advance of the tournament day; once the tournament is '
    'in progress you will not be able to enter or remove fighters. Only master rank '
    'fighters are eligible to participate in tournaments.' + CR2 +
    'To win a tournament you must win at least three of the six events. It is advisable '
    'to enter different fighters in as many events as you can to improve your chances '
    'of winning.':
        'Turnuvalar haftalık düzenlenir. Dövüş bölükleri her turnuvada bir ödül için '
        'yarışır. Bir bölük sezondaki dört turnuvanın dördünü de kazanırsa özel bir zırh '
        'takımı kazanır.' + CR2 +
        'Dövüşçüleri turnuva gününden önce kaydetmelisiniz; turnuva başladıktan sonra '
        'dövüşçü ekleyip çıkaramazsınız. Turnuvalara yalnızca usta rütbeli dövüşçüler '
        'katılabilir.' + CR2 +
        'Bir turnuvayı kazanmak için altı etkinliğin en az üçünü kazanmalısınız. '
        'Kazanma şansınızı artırmak için olabildiğince çok etkinliğe farklı dövüşçüler '
        'sokmanız yerinde olur.',
}


# Arena ussu ogreticileri exe'de bas CR ile saklaniyor. Ayni metnin CR'li
# surumunu de tabloya ekle ki tarayici her iki bicimi de bulabilsin.
for _en, _tr in list(TR.items()):
    if not _en.startswith(CR):
        TR.setdefault(CR + _en, CR + _tr)
