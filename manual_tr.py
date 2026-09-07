# -*- coding: utf-8 -*-
"""Oyun ici kilavuzun (manualkm.fds / manualcn.fds) Turkce metni.

manualkm = klavye+fare surumu, manualcn = oyun kolu surumu. 12 bolumun 6'si
iki dosyada ayni; farkli olanlar yalnizca giris (tus) anlatimlarinda ayrilir.

ISARETLEME AYNEN KORUNUR:
  [algn=2] ortala / [algn=0] sola daya
  [tcol=FFE399]...[/tcol] vurgu rengi
  [rimg=TutXxx01] gomulu gorsel
  [inpt9] vb. tus baglama yer tutuculari

TERIMLER esya ekrani ve yetenek agaciyla birebir ayni:
  Weight=Agirlik Impact=Darbe Balance=Denge Coverage=Kapsama Encumbrance=Yuk
  Slash=Kesme Crush=Ezme Pierce=Delme Thrust=Saplama
  Clarity=Duruluk Iteration=Yineleme Sustain=Surdur Abstraction=Soyutlama
  Mind=Zihin Force=Kuvvet  Thaumaturgy=Tomaturji  focus=odak  binding=bag
"""

ARMOUR = """
[algn=2][tcol=FFE399]ZIRH[/tcol]
[algn=0]
[rimg=TutArmr01]

Zırh, yaralanmaya karşı hayati bir koruma sağlar. Birkaç kat sağlam giysi bile, ölümcül bir kesik ile zararsız bir sıyrık arasındaki farkı yaratabilir.

Zırh yalnızca örttüğü yeri korur ve vücudun farklı bölgelerine birden çok katman giyilebilir. Kumaş parçaları ve benzeri eşyaları küçümsemeyin; zırhla birlikte giyilebilir, altında önemli bir dolgu oluşturur ve hiçbir zaman işe yaramaz hâle gelmezler.

Zırhlar eşyaya göre farklı kalitelerde gelir. Daha iyi sınıfları kollayın; çok sayıda zırh giymektense daha kaliteli zırh giymek yeğdir.

Ağır zırh sizi yükler. Yük, tüm hareketlerinizi olumsuz etkiler; bu etki ilk bakışta hafif görünse de kimi durumlarda belirleyici olabilir. Yükü azaltan zırh yetenekleri vardır.

Zırhların ortak özellikleri şunlardır:

[tcol=FFE399]Kapsama [/tcol]eşyanın vücudunuzu benzer bir eşyaya kıyasla ne kadar iyi örttüğünü gösterir. Neredeyse aynı iki eşyanın kapsaması farklıysa, bu küçük boşlukları ya da zayıf bölgeleri anlatır.

[tcol=FFE399]Darbe [/tcol]zırhın ne kadar kuvvet soğurabildiğini gösterir. Bu yalnızca künt kuvvete karşı korumakla kalmaz, darbeleri yumuşatarak öldürücülüklerini de azaltır. Sert ya da dolgulu zırhlar iyi darbe koruması sağlar.

[tcol=FFE399]Kesme [/tcol]zırhın kesilmesinin ne kadar güç olduğunu gösterir. Az bir kesme koruması bile daha küçük ve yüzeysel kesikler demektir; ağır zırhlar ise kesmeye karşı genellikle tümüyle geçirmezdir.

[tcol=FFE399]Ezme [/tcol]zırhı delmeden yaralanmaya yol açabilecek yoğun bir kuvvete dayanma gücüdür.

[tcol=FFE399]Delme[/tcol] zırhın delinmesinin ya da sivri uçların boşluklardan ve zayıf bölgelerden içeri girmesinin ne kadar güç olduğunu gösterir.

[tcol=FFE399]Yük[/tcol] zırhın hareketinizi ne kadar kısıtladığıdır. Bu; ağırlığı, sertliği ve duyularınız ile solunumunuz üzerindeki olumsuz etkileri kapsar.
 """

ENCOUNTERS = """
[algn=2][tcol=FFE399]KARŞILAŞMALAR[/tcol]
[algn=0]
[rimg=TutEnctr01]

Karşılaştığınız her kişi kendine özgüdür ve davranışlarınıza farklı tepki verir. Çoğu, tehdit edilmedikçe ya da ürkütülmedikçe saldırgan değildir.

Genel kural olarak, sizi tehdit saymadıklarını anlamalarına fırsat vermeden fazla yaklaşmaktan, tehditkâr hareketlerden, hatta uzun süre göz göze gelmekten kaçının. Herkes sizinle ve başkalarıyla yaşadığı önceki karşılaşmaları anımsar ve zamanla daha güçlü kanılar edinir.

Oyuncu olarak bu dünyanın sıradan bir sakinisiniz. Başkaları karşısında doğuştan bir üstünlüğünüz yok ve onları öldürmek için gerçek bir neden de yok.

Hiç değilse işe yarar bir dövüş donanımınız, özellikle de zırhınız olana dek çatışmadan kaçınmanız kesinlikle önerilir. Yara almak son derece istenmeyen bir şeydir ve kolay iyileşmez.

Bedeli ağır olacak bir dövüşten kaçmakta duraksamayın. Karşılık vermediyseniz, saldırgan sizi yeniden değerlendirip tehdit saymayabilir ve yatışabilir.
 """

HEALTH = """
[algn=2][tcol=FFE399]SAĞLIK[/tcol]
[algn=0]
[rimg=TutHelth01]

Sağlık, dayanıklılık ve yaralanma olmak üzere ikiye ayrılır. Dayanıklılık çubuğunuzda sarı renkle gösterilir ve orta şiddetteki darbeler gibi kalıcı yaralanmaya yol açmayan etkilerle eksilir. Çubuğun bir bölümü kızardığında bu yaralanmayı gösterir.

Dayanıklılık tümüyle tükendiğinde karakter bilincini yitirir, ama sonuçta hayatta kalır. Dayanıklılık hızla toparlanır; ne var ki yaralanma, ne kadarının geri kazanılabileceğini sınırlar.

Yaralanma zamanla ölüme götürür ve tedavisi kolay değildir. Yaralarınızdan kurtulmak için fırsatlar bulacaksınız, ama buna bel bağlamamalısınız. Yara almaktan ne pahasına olursa olsun kaçınmalısınız.

Zırh, hem yaralanmadan korunmada hem de darbeleri hafifletmede temel bir rol oynar. Yeterli zırhınız yokken öldürücü silahlarla dövüşmekten son derece sakının.
 """

SAVING = """
[algn=2][tcol=FFE399]KAYIT[/tcol]
[algn=0]
İlerlemeniz düzenli olarak kaydedilir; istediğiniz an çıkıp kaldığınız yere dönebilirsiniz. Zamanda geri gidip hatalarınızı geri almak için elle kaydedip yükleyemezsiniz. Ölümden ve yaralanmadan akıllıca kaçınmak oyunun temel bir parçasıdır.

Ayarlardan açabileceğiniz, isteğe bağlı kayıt noktaları vardır. Bunlar oyunun çeşitli yerlerinde ilerlemenizi kalıcı olarak kaydeder. Karakteriniz ölürse son kayıt noktasına dönebilirsiniz.

Dilediğiniz kadar oyun başlatabilirsiniz, hepsi kaydedilir. Hangisini oynayacağınızı devam ekranından seçersiniz.
 """

SHIELDS = """
[algn=2][tcol=FFE399]KALKANLAR[/tcol]
[algn=0]
[rimg=TutShld01]

Kalkanlar saldırıları savuşturmakta çok başarılıdır; ayrıca yalın birer fiziksel engel olarak edilgen bir koruma da sağlarlar.

Kalkanlar çeşitli biçim ve boyutlarda gelir. Küçük kalkanlar hafif ve hızlıdır, saldırgan bir oyunu destekler; büyük kalkanlar genellikle hantaldır ama hem etkin hem edilgen olarak güçlü koruma sunar.

Kalkanla bloklamanın kendine özgü bir dayanıklılık düzeni vardır. Ağır darbeleri üst üste bloklamak, özellikle de beklenmedik olanları karşılamak sizi yorar. Bu, sonraki blokları yavaşlatır ve darbe soğurma gücünüzü düşürür.

Kalkan kullanımını belirgin biçimde geliştiren pek çok yetenek tekniği eğitilebilir. Usta bir kalkan kullanıcısı açık yaratır, aynı anda hem saldırır hem savunur.

Kalkanların ortak özellikleri şunlardır:

[tcol=FFE399]Ağırlık[/tcol] kalkanı ne hızda kullanabildiğinizi etkiler.

[tcol=FFE399]Darbe[/tcol] kalkanın, kolunuzu ve gövdenizi korumak için güçlü kuvvetleri ne kadar iyi soğurabildiğidir.

[tcol=FFE399]Yük[/tcol] kalkanın kütlesi ve hacmi yüzünden hareketlerinizi ne kadar kısıtladığıdır.
 """

WEAPONS = """
[algn=2][tcol=FFE399]SİLAHLAR[/tcol]
[algn=0]
[rimg=TutWepns01]

Exanima'daki silahlar davranış bakımından birbirinden çok farklıdır. Bir silahın biçimi, uzunluğu ve kendine özgü dengesi çoğu zaman ekranda görünen değerlerden daha önemlidir. Kişisel tercih ve deneyim de belirleyicidir.

Silahlar ve diğer nesneler çarpışma kutusu kullanmaz; çarpışmalar silahın gördüğünüz biçimine göre hesaplanır. Hasar tümüyle darbenin kuvveti ve geometrisiyle belirlenir.

Kılıçlar çeviktir ve tüm uzunluğuyla keser; baltalar ağır darbeler indirir, ama yalnızca başıyla vurursa — ki bu baş, bloklanmaya çalışılan bir silahın ötesine de uzanabilir; gürzler ve çekiçler ağır zırhın içinden bile ciddi hasar verebilir. Her birinin ayrı üstünlükleri ve zayıflıkları olan pek çok silah vardır.

Silahların ortak özellikleri şunlardır:

[tcol=FFE399]Ağırlık[/tcol] doğrudan silahın kütlesidir. Ağır silahlar genellikle daha yavaştır ama daha sert vurur.

[tcol=FFE399]Denge [/tcol]silahın ne kadar çabuk yanıt verdiğini gösterir. Dengeli silahlar yeni hareketlere daha hızlı geçer.

[tcol=FFE399]Darbe [/tcol]bir silahın genellikle ne kadar kuvvet aktarabildiğini anlatır. Darbeler birini bilincinden edebilir ve kısa süreli iş göremezlik yaratabilir, ama aşırı ağır olmadıkça kalıcı yaralanmaya yol açmaz. Darbe kuvveti, diğer hasar türlerinin etkililiğinde de önemli rol oynar.

[tcol=FFE399]Kesme [/tcol]silahın ne kadar keskin olduğunu gösterir. Kesme hasarı çok az kuvvetle bile kesebilir, ne var ki bu tür kesikler çoğu zırhla kolayca hafifletilir.

[tcol=FFE399]Delme [/tcol]hasarı sivri uçlarla verilir. Delme, zırhtaki küçük boşluklardan içeri geçip hasar vermekte daha başarılıdır.

[tcol=FFE399]Ezme [/tcol]hasarı ağır zırhın içinden bile önemli kuvvet aktarabilir; ancak etkili olması için özellikle sert darbeler gerekir.

[tcol=FFE399]Saplama [/tcol]saplayarak verilen delme hasarıdır. Ne var ki saplamalar bir miktar darbe hasarı da verir ve duruma göre kesme hasarı uygulayabilir.
 """

# ---------------------------------------------------------------- km / cn farkli

COMBAT_ORTAK_BAS = """
[algn=2][tcol=FFE399]DÖVÜŞ[/tcol]
[algn=0]
Bu oyun, tüm hareketlerin ve sonuçların sabit animasyonlar ve basit kurallar yerine bir fizik benzetimiyle belirlendiği kendine özgü bir dövüş düzeni sunar.

Girdileriniz, karakterinizin hareketleri ve bedenine etki eden fizikle uyum içinde çalışmalıdır. Bu, bilinçli bir alıştırma gerektirir; ama zamanla akıcı ve sezgisel gelecektir.


[algn=2][tcol=FFE399]MANEVRA[/tcol]

[rimg=TutCmbt01]
[algn=0]
Hareket yalnızca konumunuzu belirlemez, tüm devinimin temel bir parçasıdır. Karakterinizin bedeninin ağırlığı ve momentumu vardır; ağırlığınızı gelişigüzel savurursanız, tıpkı gerçek dünyada olacağı gibi tökezler ve beceriksizce çırpınırsınız.

Gereğinden fazla hareket etmeyin; dengeli ve hazır durun ki gerektiğinde gerektiği gibi hareket edebilesiniz. Hareketleriniz saldırılarınızla ve diğer eylemlerinizle uyumlu olmalıdır. Başka bir oyunda tek bir tuş eksiksiz bir hareketi yapabilir; burada kendi hareketlerinizi girdileri birleştirerek siz kurarsınız.
"""

COMBAT_ORTAK_SON = """

[algn=2][tcol=FFE399]SALDIRI[/tcol]

[rimg=TutCmbt02]
[algn=0]
Hasar, çarpışmadaki kuvvetlerle belirlenir. Ayak işi ve beden hareketi çok önemlidir; gücün çoğu kollarınızdan değil bedeninizden gelir. Saldırırken bedeninizi saldırıyla birlikte hareket ettirmeli ve döndürmelisiniz. Uyumsuz saldırılar hem güçsüz olur hem de beceriksiz görünür.
{saldiri}
Saldırınızı kesmek için tuşu istediğiniz an bırakabilirsiniz. Bu, aldatma yapmak ya da savunmaya geçmek için kullanılabilir. İyi bir neden olmadan silahınızı savurmak istemezsiniz; bırakıp en kısa sürede toparlanın.
{saplama}
Ne kadar sert vurduğunuz, silahınızın hangi bölümüyle, hangi açıyla, rakibinize nereden vurduğunuz ve orada ne kadar zırh taşıdığı — hepsi belirleyicidir. Saldırı, isabet ve taktik ister. Hız önemli değildir; acele etmeyin ve vuruşunuzu değerli kılın. Yerini bulmuş tek bir darbe dövüşü bitirebilir.


[algn=2][tcol=FFE399]SAVUNMA[/tcol]

[rimg=TutCmbt03]
[algn=0]
Saldırmadığınız sürece savunmaya ve savuşturmaya çalışırsınız. Bunun yerine savunmak için saldırıyı istediğiniz anda bırakabilirsiniz. Savuşturmayı başaramasanız bile savunurken daha az açık verirsiniz.

Savuşturma ve bloklama iki uçlu eylemler değildir; duruş ve açılar önemlidir, sonucu belirleyen de sonunda fiziktir.

Saldırılardan sıyrılabilir ya da tehditlerini azaltacak biçimde hareket edebilirsiniz. Örneğin bir saldırının içine doğru hareket etmek, silahın kolunu ya da sapını kendi bedeninizle bloklamanızı veya darbenin gücünü düşürmenizi sağlayabilir.
 """

COMBAT_KM = COMBAT_ORTAK_BAS + """
Savaş moduna girmek için [inpt9] tuşuna basın. Artık nişangâh karakterinizi döndürür; adımlarınızı, saldırılarınızı ve savuşturmalarınızı yönlendirir. İlerlemek için İleri, geri çekilmek için Geri, hedefinizin çevresinde dönmek için Sol ve Sağ tuşlarına basın.

Hızlı ve denetimli adımlar atmak için hareket tuşlarına dokunun. Tuşları basılı tutmak, toparlanması daha uzun süren büyük atılımlar ya da hamleler yapar. Bu atılım davranışını kontrollerden değiştirebilirsiniz.

""" + COMBAT_ORTAK_SON.format(
    saldiri="""
Bir saldırı başlatmak için sol fare tuşunu basılı tutun. Tuşa basmadan önce nişangâhı karakterinizin soluna götürürseniz soldan saldırırsınız. Basıp bıraktıktan sonra tekrar basılı tutarsanız yukarıdan savurursunuz.
""",
    saplama="""
Saplama yapmak için [inpt13] tuşunu basılı tutup sol fare tuşuna basın. Saplarken nişangâhla sürekli nişan alır, rakibinizin belirli bir noktasını hedeflersiniz.
""")

COMBAT_CN = COMBAT_ORTAK_BAS + """
Savaş moduna girmek için [tcol=FFE399]Savaş modu[/tcol] tuşuna basın. Artık nişangâh karakterinizi döndürür, saldırılarınızı ve savuşturmalarınızı yönlendirir. [tcol=FFE399]Hareket[/tcol] artık ayak işinizi denetler; bu, baktığınız yönden bağımsızdır.

Hızlı ve denetimli adımlar atmak için küçük hareket girdileri kullanın. Daha büyük girdiler, toparlanması daha uzun süren geniş atılımlar ya da hamleler yapar.

""" + COMBAT_ORTAK_SON.format(
    saldiri="""
Bir saldırı başlatmak için [tcol=FFE399]Saldır[/tcol] tuşunu basılı tutun. Tuşa basmadan önce nişangâhı karakterinizin soluna götürürseniz soldan saldırırsınız. Basıp bıraktıktan sonra tekrar basılı tutarsanız yukarıdan savurursunuz.
""",
    saplama="""
Saplama yapmak için [tcol=FFE399]Yardımcı eylem[/tcol] tuşunu basılı tutup [tcol=FFE399]Saldır[/tcol] tuşuna basın. Saplarken nişangâhla sürekli nişan alır, rakibinizin belirli bir noktasını hedeflersiniz.
""")

INTERACTION_KM = """
[algn=2][tcol=FFE399]ETKİLEŞİM[/tcol]
[algn=0]
[rimg=TutIntr01]

Nesneleri hareket ettirebilir; kapı ve kol gibi şeyleri yalnızca fareyle sürükleyerek çalıştırabilirsiniz. Hafif nesneleri taşırken hareket tuşlarıyla döndürebilirsiniz.

Bir nesneyi etkileşim menzilinin ötesine ya da geçersiz bir konuma taşımaya çalışırsanız imleç bunu belli edecek biçimde değişir.

İncelemek ve açıklamasını görmek için bir nesneye tıklayın. Açıklamayı açık tutmak için üzerine tıklayın. Herhangi bir pencereyi kapatmak için sağ tıklayın.

Çift tıklamak anahtarları ve tüketilebilir eşyaları kullanır, kapları açar ve cesetleri arar.
Yeni bir yere geçiren bazı büyük kapılar da böyle çalıştırılır.

Bazı eylemler bir hedef ister ve imleç nişangâha dönüşür. Örneğin bir anahtara çift tıklayıp neyi açmak istediğinizi seçmelisiniz.
 """

INTERACTION_CN = """
[algn=2][tcol=FFE399]ETKİLEŞİM[/tcol]
[algn=0]
[rimg=TutIntr01]

Nesneleri hareket ettirebilir; kapı ve kol gibi şeyleri yalnızca imleçle sürükleyerek çalıştırabilirsiniz. Hafif nesneleri taşırken [tcol=FFE399]Hareket[/tcol] ile döndürebilirsiniz.

Bir nesneyi etkileşim menzilinin ötesine ya da geçersiz bir konuma taşımaya çalışırsanız imleç bunu belli edecek biçimde değişir.

İncelemek ve açıklamasını görmek için bir nesneye [tcol=FFE399]tıklayın[/tcol]. Açıklamayı açık tutmak için üzerine tıklayın. İmleç pencerenin üzerindeyken [tcol=FFE399]Kapat[/tcol] ile herhangi bir pencereyi kapatın.

Çift tıklamak anahtarları ve tüketilebilir eşyaları kullanır, kapları açar ve cesetleri arar. Yeni bir yere geçiren bazı büyük kapılar da böyle çalıştırılır.

Bazı eylemler bir hedef ister ve imleç nişangâha dönüşür. Örneğin bir anahtara çift tıklayıp neyi açmak istediğinizi seçmelisiniz.
 """

INVENTORY_SON = """
Yük, giydiğiniz eşyalarla artar; kuşanılmamış eşyalar yüke katkı yapmaz.

Yine de karakterinizin taşıyabileceği miktarın bir sınırı vardır ve buna giydikleri de dâhildir. Taşınabilir kaplar bu sınırı yükseltmeye yardımcı olabilir.
 """

INVENTORY_KM = """
[algn=2][tcol=FFE399]ENVANTER[/tcol]
[algn=0]
[rimg=TutInvtr01]

Envanterinizi açmak için [inpt10] tuşuna basın. Eşyaları kuşanmak için karakterin üzerine, yanınızda taşımak için aşağıdaki alana sürükleyin.

Ellerinize birincil ve ikincil olmak üzere iki eşya takımı kuşanabilir, sonra [inpt14] tuşuna basarak aralarında geçiş yapabilirsiniz.

""" + INVENTORY_SON

INVENTORY_CN = """
[algn=2][tcol=FFE399]ENVANTER[/tcol]
[algn=0]
[rimg=TutInvtr01]

Envanterinizi açmak için [tcol=FFE399]Envanter[/tcol] tuşuna basın. Eşyaları kuşanmak için karakterin üzerine, yanınızda taşımak için aşağıdaki alana sürükleyin.

Ellerinize birincil ve ikincil olmak üzere iki eşya takımı kuşanabilir, sonra [tcol=FFE399]Silahı çevir[/tcol] tuşuna basarak aralarında geçiş yapabilirsiniz.

""" + INVENTORY_SON

MOVEMENT_KM = """
[algn=2][tcol=FFE399]HAREKET[/tcol]
[algn=0]
[rimg=TutMvmnt01]

Hareket sağ fare tuşuyla yapılır. Koşmak için imleci daha uzağa götürün. İmleç uzaktayken varsayılan olarak koşarsınız; tam hızda koşmak için [inpt4] tuşunu basılı tutun.

Tam hızda koşmak bazı durumlarda son derece önemli olabilir. Bir şeyden kaçmanız ya da sınırlı sürede belli bir yolu almanız gerekebilir.

Fareyle başka bir eylem yaparken karakterinizin konumunu düzeltmeniz gerekirse hareket tuşlarını kullanabilirsiniz. Bunu ana giriş yöntemi olarak kullanmanız kesinlikle önerilmez; hızlı ve isabetli dönmeye ya da tam hızda koşmaya elvermez.
 """

MOVEMENT_CN = """
[algn=2][tcol=FFE399]HAREKET[/tcol]
[algn=0]
[rimg=TutMvmnt01]

Hareket denetimiyle yürüyebilir, koşabilir ya da tam hızda koşabilirsiniz. Koşmak için daha büyük girdiler kullanın; daha hızlı koşmak için koşma tuşunu basılı tutun. Koşma tuşunu basılı tutmak, dövüş sırasında da koşmanızı sağlar.

Tam hızda koşmak bazı durumlarda son derece önemli olabilir. Bir şeyden kaçmanız ya da sınırlı sürede belli bir yolu almanız gerekebilir.
 """

SKILLS_SON = """
Her yetenekte en çok 5 teknik eğitebilirsiniz. Yeni bir eğitime hazır olduğunuzda boş teknik yuvalarında artı simgesi görünür. Yeni bir teknik seçtiğinizde eğitim başlar; tamamlandığında tekniği kullanabilirsiniz.

Deneyim, yaptığınız ve keşfettiğiniz her şeyle kazanılır. Keşif, okumak ve yeni bilgi edinmek, gizli nesneleri bulmak ve yeni eşyaları ilk kez kullanmak en büyük deneyim kaynağıdır. Zayıf rakiplerle dövüşmek yok denecek kadar az deneyim verir.

Deneyimin işlenip özümsenmesi zaman alır. Kısa sürede çok deneyim kazanırsanız etkilerini görmeniz biraz zaman alabilir. Yetenek eğitiyor olmanız önemlidir, yoksa deneyim kullanılmaz.

Kazandığınız tüm deneyimin kabaca dörtte biri Genel Deneyiminize gider. Bu, yeni karakterlere başlangıç deneyimi sağlar ve kayıtlı bir oyuna dönerken var olan tüm karakterlere geriye dönük olarak da uygulanır.
 """

SKILLS_KM = """
[algn=2][tcol=FFE399]YETENEKLER[/tcol]
[algn=0]
Karakterinizin yeteneklerini görmek ve yönetmek için [inpt11] tuşuna basın.

""" + SKILLS_SON

SKILLS_CN = """
[algn=2][tcol=FFE399]YETENEKLER[/tcol]
[algn=0]
Karakterinizin yeteneklerini görmek ve yönetmek için [tcol=FFE399]Yetenek[/tcol] tuşuna basın.

""" + SKILLS_SON

THAUM_BAS = """
[algn=2][tcol=FFE399]TÖMATURJİ[/tcol]
[algn=0]
Bazı karakterler, Tömaturji olarak bilinen zihinsel yetilere erişebilir.
"""

THAUM_SON = """
Güce bağlı olarak hedeflemek için imleci kullanmanız gerekebilir; isabetiniz de önemli olabilir ve gücün şiddetini etkiler. Zihin için bu genellikle hedefin başıdır.

Belirli güçleri öğrenmek ve yenilerini keşfetmek için belirli karakter yetenekleri gerekebilir. Yetenekler ayrıca güçlerinizi daha verimli kullanmanıza yardımcı olur.


[algn=2][tcol=FFE399]ODAK[/tcol]
[algn=0]
Güç kullanma yetiniz, ekranınızın altındaki mavi çubukla gösterilen zihinsel odağınızla belirlenir. Bu, her güç kullandığınızda tükenir ve zamanla yavaşça toparlanır.

Güçler odağı üç ana yolla tüketir:

[tcol=FFE399]Anlık[/tcol] güçler yalnızca sabit bir miktar tüketir;

[tcol=FFE399]Sürdürülen[/tcol] güçler süreleri boyunca odağı azar azar kullanır;

[tcol=FFE399]Sürekli[/tcol] güçler, bozulana ya da bırakılana dek odağınızın bir bölümünü ayırır.

Birkaç yetenek tekniği odağınızı etkiler. [tcol=FFE399]Duruluk[/tcol] odak toparlanmanızı artırır, [tcol=FFE399]Yineleme[/tcol] aynı gücün sonraki kullanımlarında harcanan odağı azaltır, [tcol=FFE399]Sürdür[/tcol] sürdürülen güçlerin harcadığı odağı azaltır, [tcol=FFE399]Soyutlama[/tcol] ise sürekli güçlerin ayırdığı odağı azaltır.
 """

THAUM_KM = THAUM_BAS + """
Böyle bir karakter oynuyorsanız, o anki güçlerinizi görmek, hangilerini öğreneceğinizi seçmek ve kullanıma hazırlamak için [inpt17] tuşuna basabilirsiniz. Açıklamasını görmek için her gücün üzerine gelin.

Hazırladığınız ve etkin olan güçleri görmek için [inpt16] tuşuna, ardından bir gücü kullanmak ya da açıp kapatmak için karşılık gelen sayı tuşuna basın.

""" + THAUM_SON

THAUM_CN = THAUM_BAS + """
Böyle bir karakter oynuyorsanız, o anki güçlerinizi görmek, hangilerini öğreneceğinizi seçmek ve kullanıma hazırlamak için [tcol=FFE399]Güçler[/tcol] tuşunu basılı tutabilirsiniz. Açıklamasını görmek için her gücün üzerine gelin.

Hazırladığınız ve etkin olan güçleri görmek için [tcol=FFE399]Güçler[/tcol] tuşuna basın; [tcol=FFE399]Hareket[/tcol] ile bir güç seçebilirsiniz. [tcol=FFE399]Güçler[/tcol] tuşuna yeniden basarsanız, [tcol=FFE399]Güç kullan[/tcol] tuşuna bastığınızda kullanılacak güç bu olur. Ayrıca seçmeden doğrudan kullanmak için [tcol=FFE399]Güç kullan[/tcol] tuşuna basabilirsiniz.

""" + THAUM_SON

ORTAK = {'armour': ARMOUR, 'encounters': ENCOUNTERS, 'health': HEALTH,
         'saving': SAVING, 'shields': SHIELDS, 'weapons': WEAPONS}

METIN = {
    'manualkm.fds': dict(ORTAK, combat=COMBAT_KM, interaction=INTERACTION_KM,
                         inventory=INVENTORY_KM, movement=MOVEMENT_KM,
                         skills=SKILLS_KM, thaumaturgy=THAUM_KM),
    'manualcn.fds': dict(ORTAK, combat=COMBAT_CN, interaction=INTERACTION_CN,
                         inventory=INVENTORY_CN, movement=MOVEMENT_CN,
                         skills=SKILLS_CN, thaumaturgy=THAUM_CN),
}
