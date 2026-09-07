# -*- coding: utf-8 -*-
"""charroles.rdb icindeki NPC diyaloglarinin Turkce karsiliklari.

IKI AYRI AGIZ
  Derrin  - kirsal, egitimsiz, batil inancli bir irgat. Devrik cumleler,
            "sanirim/bilmem/valla", kisa ve dolaysiz konusur.
  Oyuncu  - egitimli, olculu, zaman zaman kucumseyen bir tomaturjist.
  Ikisi de birbirine "sen" der.

TERIMLER
  thaumaturge -> tomaturjist        thaumer (Derrin'in argosu) -> tomaci
  shaper -> (bag) sekillendiricisi  Order of Thaumaturges -> Tomaturjistler Tarikati
  necromancer -> nekromant          binding -> bag
  undead / dead ones -> oluler      underworld -> yeralti dunyasi
  the hells -> cehennemler          portal/gateway -> gecit
  farm hand -> irgat                hedge witch -> koy cadisi

{Actor[0].Name} ve {Actor[1].Name} yer tutuculari ile satir ici \\r\\n AYNEN korunur.
Eslesmeyen anahtarlar sessizce Ingilizce kalir; tr_charroles.py kapsama raporu verir.
"""

TR = {
    "A hole in the ground. That's where we are.":
        'Yerdeki bir delik. Bulunduğumuz yer orası.',
    'A memory I think. It scared me.':
        'Bir anı sanırım. Beni korkuttu.',
    "A per... Never mind. But these dead ones then? What's binding them?":
        'Sür... Boş ver. Peki ya şu ölüler? Onları ne bağlıyor?',
    "A perpetual binding? It's nothing more than an idea, quite impossible.":
        'Kalıcı bir bağ mı? Bu bir fikirden ibaret, tümüyle imkânsız.',
    "A shaper of minds can do good. Give peace to those who won't find it of their own, dispel fears and bring harmony where there is discord. They can be healers of the mind.":
        'Zihin şekillendiricisi iyilik de yapabilir. Kendi başına huzur bulamayanlara huzur verir, korkuları dağıtır, kavga olan yere uyum getirir. Zihnin şifacıları olabilirler.',
    'A spy? No!\r\nI guess, sometimes. People act normal near me, I hear things, they tell me things.':
        'Casus mu? Yok canım!\r\nBazen, sanırım. Yanımda rahat olurlar, bir şeyler duyarım, anlatırlar.',
    'A thaumer? It seems I have the basic talent.':
        'Tömacı mı? Anlaşılan temel yetenek bende.',
    'Again?':
        'Yine?',
    'All I know is I came through a hole in the ground.':
        'Tek bildiğim, yerdeki bir delikten geldiğim.',
    "All I've got is this stick though.":
        'Ama elimde bu sopa var, hepsi bu.',
    'All in order?':
        'Sorun yok mu?',
    "All this, it's exciting, you know. The exploring, even the danger.":
        'Bütün bunlar heyecanlı, biliyor musun. Keşfetmek, tehlike bile.',
    'Alright, so what do you call someone who has this talent?':
        'Peki, bu yeteneği olan birine ne diyorsunuz?',
    'Alright.':
        'Peki.',
    "Alright. I'll come with you.":
        'Peki. Seninle geliyorum.',
    "Alright. I'll try.":
        'Peki. Deneyeceğim.',
    'Alright. We go together then.':
        'Peki. Beraber yola çıkarız.',
    "Alright. You're not the type I usually do this with, so I'll just stop.":
        'Peki. Bunu genelde senin gibileriyle yapmam zaten, keseyim.',
    'And does you being here have something to do with all this?':
        'Peki senin burada olmanın bütün bunlarla bir ilgisi var mı?',
    "And it's dark.":
        'Hem karanlık.',
    'And so they found you, and here you are.':
        'Sonra da onlar seni buldu ve buradasın.',
    'And to you.':
        'Sana da.',
    'And who threw you in the hole?':
        'Peki seni deliğe kim attı?',
    'And yet curiosity is what leads us to wisdom.':
        'Yine de bizi bilgeliğe götüren şey meraktır.',
    'And you ran from something half dead with a stick. Pah.':
        'Sen de elinde sopayla yarı ölü bir şeyden kaçtın. Pöh.',
    "Ardent, the powers that be. They don't want us down here, for a start, but the true reason I don't know.":
        'Ardent, yani erk sahipleri. Bir kere burada olmamızı istemiyorlar, ama asıl nedenini bilmiyorum.',
    'Are you able to fight?':
        'Dövüşebiliyor musun?',
    'Are you alright?':
        'İyi misin?',
    'Are you hurt?':
        'Yaran var mı?',
    'Are you well?':
        'İyi misin?',
    'Bandits.':
        'Eşkıya.',
    "Best you don't know and hope we don't meet one.":
        'Bilmesen daha iyi; umarım birine denk gelmeyiz.',
    'But I am. Let us put it behind us and join our efforts.':
        'Ama öyleyim. Bunu geride bırakıp güçleri birleştirelim.',
    "But don't they only work for a time, then need turning over for a time?":
        'Ama onlar bir süre çalışıp sonra bir süre dinlendirilmiyor mu?',
    'But what about the dead ones?':
        'Peki ya ölüler?',
    'By bandits. They robbed me and threw me down a hole in the ground.':
        'Haydutlar. Beni soydular, sonra da yerdeki delikten aşağı attılar.',
    'By people who grow tired of farm hands asking too many questions.':
        'Fazla soru soran ırgatlardan bıkan kişiler.',
    'Calm down, it was just a joke.':
        'Sakin ol, şakaydı.',
    "Can't just stay here, we should look around.":
        'Burada öylece duramayız, etrafa bakmalıyız.',
    "Can't. Hole is too high to reach.":
        'Olmaz. Delik yüksek, ulaşamam.',
    "Can't. The hole is too high to reach.":
        'Olmaz. Delik çok yüksek, uzanamayız.',
    "Clearly they wanted to be rid of you, perhaps they didn't have the stomach for it.":
        'Senden kurtulmak istedikleri açık; belki de gözleri kesmedi.',
    "Clearly you are practiced in your deception, but I'm not easily fooled.":
        'Yalanda ustalaştığın belli, ama beni kandırmak o kadar kolay değil.',
    "Clever that.\r\nAlright, let's keep going.":
        'Akıllıcaymış.\r\nPeki, devam edelim.',
    'Come with me Derrin, we can find a way out together.':
        'Benimle gel Derrin, birlikte bir çıkış bulabiliriz.',
    "Come with me, I doubt you'll survive this on your own.":
        'Benimle gel; bunu tek başına atlatacağını sanmıyorum.',
    "Come with me, I'll get us out of here.":
        'Benimle gel, bizi buradan çıkarırım.',
    'Come with me.':
        'Benimle gel.',
    'Command the dead, turn us against each other, fill us with dread, or simply make us do their bidding.':
        'Ölülere hükmeder, bizi birbirimize düşürür, içimizi dehşetle doldurur ya da düpedüz buyruğuna sokar.',
    'Damn you!':
        'Yuh sana!',
    'Demons could come out right now!':
        'Şu anda iblisler çıkabilir!',
    'Demons do not live under ground.':
        'İblisler yeraltında yaşamaz.',
    'Demons!\r\nI told you!':
        'İblisler!\r\nDemiştim!',
    "Derrin, I can't leave you on your own. Come with me.":
        'Derrin, seni burada yalnız bırakamam. Benimle gel.',
    "Derrin, I won't leave you on your own. Come with me.":
        'Derrin, seni yalnız bırakmayacağım. Benimle gel.',
    'Derrin, clearly you are not just a farm hand. What are you hiding?':
        'Derrin, sıradan bir ırgat olmadığın çok açık. Ne saklıyorsun?',
    'Derrin, come with me. Let us work together.':
        'Derrin, benimle gel. Birlikte çalışalım.',
    'Derrin, we must enter the portal.':
        'Derrin, geçide girmemiz gerek.',
    'Derrin, we need to find a way out of here.':
        'Derrin, buradan bir çıkış bulmamız gerek.',
    'Derrin.':
        'Derrin.',
    "Derrin.\r\nI'm afraid I don't remember much, but you can call me {Actor[1].Name}.":
        'Derrin.\r\nMaalesef pek bir şey anımsamıyorum. Bana {Actor[1].Name} diyebilirsin.',
    'Derrin. I could use your help.':
        'Derrin. Yardımın işime yarar.',
    'Did you know her well?':
        'Onu iyi tanır mıydın?',
    "Didn't I just tell you that?":
        'Bunu az önce söylemedim mi?',
    'Do as you wish.':
        'Nasıl istersen.',
    'Do you consider me a friend?':
        'Beni dost sayıyor musun?',
    'Do you intend to make yourself useful?':
        'İşe yaramaya niyetin var mı?',
    'Do you know how to fight?':
        'Dövüşmeyi biliyor musun?',
    'Do you remember something?':
        'Bir şey hatırlıyor musun?',
    'Do you truly believe such things?':
        'Bunlara gerçekten inanıyor musun?',
    "Don't get too excited. The danger is real.":
        'Fazla heyecanlanma. Tehlike gerçek.',
    "Don't leave me here! I won't make it.":
        'Beni burada bırakma! Ben sağ çıkamam.',
    "Don't leave your life to chance. Come.":
        'Canını rastlantıya bırakma. Gel.',
    "Don't talk nonsense Derrin.":
        'Saçmalama Derrin.',
    "Don't think I'll be much use, but I'll try to keep up.":
        'Pek işine yararım sanmam ama ayak uydurmaya çalışırım.',
    "Don't touch anything unless I say so.":
        'Ben söylemedikçe hiçbir şeye dokunma.',
    "Don't touch anything unless I say so. Let's be on our way.":
        'Ben söylemedikçe hiçbir şeye dokunma. Yola koyulalım.',
    "Don't worry about them, they seem placid.":
        'Onları dert etme, uysal görünüyorlar.',
    "Don't worry, I can handle these undead.":
        'Merak etme, bu ölülerle başa çıkarım.',
    'Everyone knows of the underworld!':
        'Yeraltı dünyasını herkes bilir!',
    'Fair enough.':
        'Doğru söz.',
    "Fair point. Let's turn our thoughts to getting out of here.":
        'Yerinde bir söz. Aklımızı buradan çıkmaya verelim.',
    'Find your courage.\r\nI must be going.':
        'Cesaretini topla.\r\nArtık gitmeliyim.',
    'Fine.':
        'Peki.',
    'Fine. But give us a chance before choosing flight.':
        'Peki. Ama kaçmayı seçmeden önce bize bir şans ver.',
    'Fine. Stay away from me.':
        'Peki. Benden uzak dur.',
    'Follow me.':
        'Beni izle.',
    'Follow.':
        'Gel.',
    'Forbidden? Why? By whom?':
        'Yasak mı? Neden? Kim?',
    "Forgive me, I don't know what came over me.":
        'Bağışla, bana ne olduğunu bilmiyorum.',
    'Get away from me!':
        'Çekil yanımdan!',
    'Go away!':
        'Uzaklaş!',
    "Gods below, I guess you're right.\r\nI thought I knew some others, but with her I was sure.":
        'Alttaki tanrılar aşkına, galiba haklısın.\r\nBaşkalarını tanıdım sandım ama ondan emindim.',
    "Gods below, I hope I won't have need.":
        'Tanrılar aşkına, umarım gerek kalmaz.',
    'Gods below, that... \r\nThat monster!':
        'Tanrılar aşkına, o... \r\nO canavar!',
    'Good luck then.':
        'Peki, bol şans.',
    'Good luck to you.':
        'Sana iyi şanslar.',
    "Good thing they didn't then.":
        'İyi ki de kesmemiş.',
    'Good.':
        'Peki.',
    "Good. I don't want to be.":
        'Güzel. Zaten istemiyorum.',
    "Good. Let's go.":
        'Güzel. Gidelim.',
    "Good. You'll let me be then?":
        'Güzel. Rahat bırakır mısın?',
    'Goodbye Derrin.':
        'Elveda Derrin.',
    'Goodbye.':
        'Elveda.',
    "Guess it's time to finally learn.":
        'Galiba artık öğrenme vakti geldi.',
    'Ha.\r\nWell, reckon I might not get another chance.':
        'Ha.\r\nValla, bir daha fırsat bulamam herhâlde.',
    'Ha. So you will follow.':
        'Ha. Demek geliyorsun.',
    'Head hurts again?':
        'Yine baş ağrısı?',
    'Hello?':
        'Selam?',
    'Help me. Together we can escape.':
        'Yardım et. Birlikte kaçabiliriz.',
    'Help yourself, man.':
        'Buyur, keyfine bak.',
    "Help?\r\nI don't think so.":
        'Yardım mı?\r\nHiç sanmam.',
    'Hey, you!':
        'Hey, sen!',
    "Hitting your head can make you forget stuff. I've heard.":
        'Kafanı çarpınca insan bir şeyleri unuturmuş. Duymuştum.',
    "Hopefully we won't run into much trouble.":
        'Umarım başımıza pek iş açılmaz.',
    "How about you go in, and if you don't come back I'll know.":
        'Sen girsene; dönmezsen ben de anlamış olurum.',
    'How are you doing?':
        'Nasılsın?',
    'How can you not remember your name?':
        'Kendi adını nasıl hatırlamazsın?',
    'How could you know?':
        'Nereden biliyorsun?',
    'How did you get here? Can you get out?':
        'Buraya nasıl geldin? Çıkabilir misin?',
    'How? The hole is too high to reach.':
        'Nasıl? Delik çok yüksekte kalıyor.',
    'I admit It is quite frightening. Sometimes I look at my hands and think "who is this person?"':
        'İtiraf edeyim, epey ürkütücü. Bazen ellerime bakıp "bu kişi de kim?" diye düşünüyorum.',
    "I am farm hand, but I'm also lord Ermus' man. I keep an eye on things and let him know what I see.":
        "Irgatım, ama aynı zamanda lort Ermus'un adamıyım. Etrafı kollar, gördüklerimi ona iletirim.",
    'I am quite proficient.':
        'Bu işte hayli ustayım.',
    'I can protect you, come.':
        'Seni koruyabilirim, gel.',
    "I can see what's past a door, and it's not often the stuff of nightmares.":
        'Bir kapının ardında ne var görürüm, hem de genelde kâbus gibi olmaz.',
    "I can't let you go. You might attack me when I don't expect it.":
        'Gitmene izin veremem. Ummadığım bir anda bana saldırabilirsin.',
    "I can't remember much at all. You can call me {Actor[1].Name}.":
        'Pek bir şey hatırlamıyorum. Bana {Actor[1].Name} diyebilirsin.',
    'I care little how you feel, only for what is real and true. Wherever this gateway leads, it is not to the hells.':
        'Ne hissettiğin umurumda değil, yalnızca gerçek olan. Bu geçit nereye çıkarsa çıksın, cehennemlere çıkmıyor.',
    'I certainly intend to.':
        'Kesinlikle niyetim o.',
    "I couldn't say, it flees my mind like a dream upon waking.":
        'Bilemem; uyanınca kaçan bir rüya gibi aklımdan uçuyor.',
    "I didn't cause any trouble.":
        'Kimseye zarar vermedim.',
    "I didn't do nothing!":
        'Bir şey yapmadım ki!',
    "I didn't!":
        'Yapmadım!',
    "I don't deny that demons are real, but it's not likely you'll find them here.":
        'İblislerin varlığını yadsımıyorum, ama onları burada bulman pek olası değil.',
    "I don't know how much help I am, but I'll do my best.":
        'Ne kadar faydam olur bilmem, elimden geleni yaparım.',
    "I don't know much, but I can see what's in front of me.":
        'Fazla bir şey bilmem, ama önümdekini görebiliyorum.',
    "I don't know that I'd call you friend.":
        'Sana dost der miydim, bilemiyorum.',
    "I don't know, I don't remember much.":
        'Bilmiyorum, pek bir şey aklımda yok.',
    "I don't know, it was really just a feeling.":
        'Bilmiyorum, gerçekten sadece bir histi.',
    "I don't know, it's not my concern.":
        'Bilmiyorum, beni ilgilendirmez.',
    "I don't know, probably didn't want me telling on them.":
        'Bilmem, herhâlde onları ele vermemi istemediler.',
    "I don't know. Everyone is mad all of a sudden.":
        'Bilmiyorum. Herkes birdenbire delirdi.',
    "I don't know. Hopefully it won't give ailment.":
        'Bilmem. Umarım hastalık getirmez.',
    "I don't know. I don't like it.":
        'Bilmiyorum. Hoşuma gitmedi.',
    "I don't know...":
        'Bilmiyorum...',
    "I don't mean it like that.":
        'Onu demek istemedim.',
    "I don't remember even that, I think it may be {Actor[1].Name}.":
        'Onu bile hatırlamıyorum; sanırım {Actor[1].Name} olabilir.',
    "I don't see that we have choice.":
        'Başka bir seçeneğimiz yok gibi.',
    "I don't, but alright. So how do the lamps work then?":
        'Anlamıyorum, ama olsun. Peki lambalar nasıl çalışır?',
    'I doubt there is a connection.':
        'Bağlantı olduğunu sanmıyorum.',
    'I fear I may not like who I am.':
        'Korkarım kim olduğumu beğenmem.',
    'I got attacked by Bandits. They robbed me, then threw me in here.':
        'Haydutlar saldırdı. Beni soydular, sonra da buraya attılar.',
    "I guess I'll be on my way then.":
        'Sanırım yoluma gideyim öyleyse.',
    'I guess they must be alchemical.':
        'Herhâlde simya işidir.',
    "I guess they thought we wouldn't make it out. Let's prove them wrong.":
        'Sanırım çıkamayacağımızı düşündüler. Yanıldıklarını gösterelim.',
    "I guess you're right. You seem so sure, but I have doubts.":
        'Sanırım haklısın. Sen çok eminsin, ama benim kuşkum var.',
    "I guess. I'm sorry, I'll shut up now.":
        'Sanırım. Affedersin, susuyorum artık.',
    'I had you right.':
        'Seni tanımışım.',
    "I have friends! And my Ma. Okay, Well, Ermus is the friend I care about, that's why I do it.":
        'Dostlarım var! Bir de anam. Tamam, peki, önemsediğim dost Ermus; bu yüzden yapıyorum.',
    'I have no need for you then.':
        'O hâlde sana ihtiyacım yok.',
    'I just do.':
        'Öyle işte.',
    'I know very little, someone like me would not be admitted to the order.':
        'Çok az şey bilirim; benim gibi biri tarikata alınmaz.',
    "I know what that is, it's a gateway to hell!":
        'Ne olduğunu biliyorum, cehennem kapısı o!',
    "I know you're upset, but you need my help.":
        'Kızgınsın biliyorum ama yardımım gerek.',
    "I know. I won't happen again, I swear it.":
        'Biliyorum. Bir daha olmaz, yemin ederim.',
    "I mean you no harm. I'm just confused, I don't remember anything.":
        'Sana zarar vermem. Kafam çok karışık, hiçbir şey hatırlamıyorum.',
    "I must admit I'm quite useless myself.":
        'İtiraf edeyim, ben de pek işe yaramam.',
    'I must leave.':
        'Gitmem gerek.',
    'I need to get out of here.':
        'Buradan çıkmam gerek.',
    "I really don't know.":
        'Sahiden bilmiyorum.',
    'I reckon you decide who you want to be.':
        'Bence kim olacağına sen karar verirsin.',
    "I said it in jest. Don't worry.":
        'Şaka yapıyordum. Merak etme.',
    'I say the simple truth as I see it. You are too hasty in your assumptions.':
        'Gördüğüm yalın gerçeği söylüyorum. Varsayımlarında fazla acelecisin.',
    'I see why you think as you do, but think also of the truth in what I say.':
        'Neden böyle düşündüğünü anlıyorum ama söylediklerimdeki doğruyu da düşün.',
    'I see.':
        'Peki.',
    'I see. Does your being here have something to do with all this?':
        'Anlıyorum. Senin burada olmanın tüm bunlarla bir ilgisi var mı?',
    'I see. Perhaps just a cruel way to be rid of you.':
        'Anladım. Belki de senden kurtulmanın zalim yolu.',
    'I seem to be having trouble remembering things.':
        'Galiba bir şeyleri hatırlamakta zorlanıyorum.',
    'I seem to have no memories. It might be {Actor[1].Name}, but it sounds strange to me.':
        'Hiç anım yok gibi. {Actor[1].Name} olabilir, ama bana yabancı geliyor.',
    "I suppose I've got no choice.":
        'Sanırım başka çarem yok.',
    "I suppose not. I'm just in the habit of keeping it secret.":
        'Sanırım yok. Sadece bunu gizli tutmaya alışmışım.',
    'I suppose that makes sense.':
        'Sanırım mantıklı.',
    "I suppose that makes sense. I wonder if they knew what's down here.":
        'Sanırım mantıklı. Acaba aşağıda ne olduğunu biliyorlar mıydı?',
    "I suppose we can try, but if things get bad I'm back to hiding.":
        'Deneyebiliriz sanırım, ama işler sarpa sararsa yine saklanırım.',
    "I suppose we can try, but if things get bad you're on your own.":
        'Deneyebiliriz sanırım, ama işler kötüye giderse yalnızsın.',
    'I suppose you can come with me.':
        'Sanırım benimle gelebilirsin.',
    'I suppose you did find them after all.':
        'Demek sonunda onları gerçekten buldun.',
    "I suppose. Let me know if you see anything useful. Let's go now.":
        'Sanırım. İşe yarar bir şey görürsen söyle. Hadi gidelim.',
    'I take it this is not your usual purview.':
        'Anlaşılan bu pek alışık olduğun iş değil.',
    'I think I can deal with them.':
        'Sanırım onlarla başa çıkarım.',
    'I think I may be able to handle these undead.':
        'Sanırım bu ölülerin üstesinden gelebilirim.',
    "I think I'll find my own way.":
        'Sanırım kendi yolumu bulurum.',
    "I think I'm starting to like this.":
        'Galiba bu hoşuma gitmeye başlıyor.',
    'I think it best if you stay here after all.':
        'Bence yine de burada kalman en iyisi.',
    "I think my name is {Actor[1].Name}, but I don't really remember anything at all.":
        'Sanırım adım {Actor[1].Name}, ama aslında hiçbir şey hatırlamıyorum.',
    'I think so.':
        'Sanırım.',
    "I think that's all I need to know. This doesn't concern me.":
        'Sanırım bilmem gereken bu kadar. Bu beni ilgilendirmiyor.',
    'I think we should part ways.':
        'Bence yollarımızı ayıralım.',
    'I thought you would attack me.\r\nWho are you?':
        'Bana saldıracağını sandım.\r\nSen kimsin?',
    "I wasn't saying you did...\r\nLet's just get out of here.":
        'Öyle dediğim yoktu...\r\nHadi çıkalım şuradan.',
    "I wasn't suggesting you did. Now I'm not so sure.":
        'Öyle ima etmemiştim. Şimdi o kadar emin değilim.',
    'I will continue on. If you want to turn back, I will understand.':
        'Ben devam edeceğim. Geri dönmek istersen anlarım.',
    'I will find a way out.':
        'Bir çıkış bulacağım.',
    "I will protect you. You'll be safe with me.":
        'Seni koruyacağım. Yanımda güvende olursun.',
    'I will send help for you if I can.':
        'Yapabilirsem sana yardım yollarım.',
    'I will. Best of luck to you Derrin.':
        'Yollarım. Bol şans Derrin.',
    "I woke up on the ground, I can't recall anything before then.":
        'Yerde uyandım, öncesine dair hiçbir şey anımsamıyorum.',
    "I won't harm you.\r\nWho are you?":
        'Sana zarar vermem.\r\nKimsin sen?',
    "I won't stop you. Will you tell me your name before you go?":
        'Seni durdurmayacağım. Gitmeden adını söyler misin?',
    'I wonder what happened to you.':
        'Sana ne olmuş, merak ediyorum.',
    "I worked in Ermus' father's orchards when I was little. Ermus and I became friends. We still are, we have long talks. I tell him things, he teaches me things.":
        "Küçükken Ermus'un babasının bahçelerinde çalışırdım. Ermus'la dost olduk. Hâlâ öyleyiz, uzun uzun konuşuruz. Ben ona bir şeyler anlatırım, o bana öğretir.",
    "I worked in his father's orchards as a lad, and we became friends. We still meet, in secret. I tell him what he doesn't see in his lands, he teaches me things, gives me books.":
        'Delikanlıyken babasının meyve bahçesinde çalıştım, dost olduk. Hâlâ gizlice görüşürüz. Ben ona topraklarında göremediklerini anlatırım, o bana bir şeyler öğretir, kitap verir.',
    "I'd rather focus on getting out, but take what you want.":
        'Ben çıkmaya odaklanmayı yeğlerim, ama istediğini al.',
    "I'll do my best. Only got this stick though.":
        'Elimden geleni yaparım. Bir tek bu sopa var.',
    "I'll do that.":
        'Öyle yaparım.',
    "I'll need my strength at least. I think more challenges lie ahead of us.":
        'En azından gücüme ihtiyacım olacak. Sanırım önümüzde daha çok engel var.',
    "I'll return for you, if I can.":
        'Elimden gelirse dönerim sana.',
    "I'll stay with you. For now.":
        'Seninle kalırım. Şimdilik.',
    "I'll try.":
        'Denerim.',
    "I'm Derrin. I'm just a farm hand.\r\nWhat about you?":
        'Ben Derrin. Sıradan bir ırgatım.\r\nYa sen?',
    "I'm afraid I don't remember much.":
        'Ne yazık ki pek hatırlamıyorum.',
    "I'm as mad as you are to follow you.":
        'Seni izlediğime göre ben de deliyim.',
    "I'm certain there's another way out.":
        'Başka bir çıkış olduğuna eminim.',
    "I'm fine.":
        'İyiyim.',
    "I'm fine. I think I've been here before.":
        'İyiyim. Sanırım buraya daha önce geldim.',
    "I'm going to have a look around.":
        'Etrafa bir bakacağım.',
    "I'm good.":
        'İyiyim.',
    "I'm guessing so I wouldn't tell I'd seen them.":
        'Sanırım onları gördüğümü söylemeyeyim diye.',
    "I'm here now. Come.":
        'Ben buradayım. Gel.',
    "I'm in a bad way.":
        'Durumum kötü.',
    "I'm just a farm hand with a stick! What was I to do?":
        'Elinde sopayla sıradan bir ırgatım! Ne yapsaydım?',
    "I'm looking for another way for us to get out.":
        'Çıkmamız için başka bir yol arıyorum.',
    "I'm more concerned about the necromancer.":
        'Beni asıl nekromant kaygılandırıyor.',
    "I'm no fighter.":
        'Ben dövüşemem.',
    "I'm no use, just leave me.":
        'İşe yaramam, bırak beni.',
    "I'm not so sure now. Can I come with you?":
        'Pek emin değilim artık. Seninle gelsem?',
    "I'm not sure, it just sort of comes to me. I know things, objects, ideas, but I don't recall myself doing anything before now.":
        'Emin değilim, kendiliğinden geliyor. Şeyleri, nesneleri, fikirleri biliyorum; ama şu ana dek bir şey yaptığımı anımsamıyorum.',
    "I'm not use at all. Best I stay here.":
        'Hiçbir işe yaramam. Burada kalayım.',
    "I'm not well at all.":
        'Hiç iyi değilim.',
    "I'm not. I just never saw myself doing this, but I am.":
        'Değilim. Bunu yapacağımı hiç sanmazdım, ama yapıyorum.',
    "I'm scared enough as it is.":
        'Zaten yeterince korkuyorum.',
    "I'm sorry, I'm very confused.\r\nWho are you?":
        'Affedersin, kafam çok karışık.\r\nSen kimsin?',
    "I'm sorry. I was trying to lighten the mood.":
        'Özür dilerim. Havayı yumuşatmak istemiştim.',
    "I'm sorry. I will try to send help.":
        'Üzgünüm. Yardım yollamayı denerim.',
    "I'm sorry. That must be awful to see.":
        'Üzgünüm. Bunu görmek korkunç olmalı.',
    "I'm starting to think I may not want it to. I feel the memories would not be pleasant.":
        'İstemeyebileceğimi düşünmeye başlıyorum. Anıların hoş olmayacağını hissediyorum.',
    "I'm still afeared, but maybe I'm not so weak as I thought.":
        'Hâlâ korkuyorum, ama belki sandığım kadar zayıf değilim.',
    "I'm sure it will come back to you.":
        'Eminim geri gelecektir.',
    "I'm sure you'll make yourself useful.":
        'Eminim bir işe yararsın.',
    "I'm the only ally you have Derrin. You'll die on your own.":
        'Tek dostun benim Derrin. Tek başına ölürsün.',
    "I've been better, but nothing serious.":
        'İyi günlerim de oldu, ama ciddi değil.',
    "I've had enough of you!":
        'Senden bıktım artık!',
    "I've reconsidered. We may able to help each other. Will you come?":
        'Fikrimi değiştirdim. Birbirimize yardım edebiliriz. Gelir misin?',
    "I've studied such things. You must trust me.":
        'Böyle şeyleri inceledim. Bana güvenmelisin.',
    "If I can't convince you, then so be it.":
        'Seni ikna edemiyorsam, öyle olsun.',
    "If I can't rely on you, then you're no use to me.":
        'Sana güvenemiyorsam, bana bir faydan yok.',
    'If there are undead, there is a necromancer. Close by.':
        'Ölüler varsa, nekromant da vardır. Hem de yakınlarda.',
    'If there are undead, there must a necromancer.':
        'Ölüler varsa, bir nekromant olmalı.',
    'If they get in my way, I will kill them.':
        'Yoluma çıkarlarsa öldürürüm.',
    'If you got thrown in like me, you maybe hit your noggin.\r\nThat can forget you stuff.':
        'Seni de benim gibi attılarsa kafanı çarpmışsındır.\r\nÖyle olunca insan unuturmuş.',
    "If you're not a thaumer, what are you then?":
        'Tömacı değilsen, nesin peki?',
    'If you make it, will you send help?':
        'Kurtulursan yardım yollar mısın?',
    'If you think know better, you can find your own way.':
        'Daha iyisini biliyorsan kendi yolunu bulabilirsin.',
    'In the ground? Where are we?':
        'Yerin altında mı? Neredeyiz?',
    'In truth I thought I could find the bandits and report what I saw.\r\nI did, and they found me. And so here I am.':
        'Doğrusu haydutları bulup gördüklerimi bildiririm sandım.\r\nBuldum da, sonra onlar beni buldu. İşte buradayım.',
    "Interesting. I'm not familiar with that smell.":
        'İlginç. Bu koku bana yabancı.',
    'Interesting. Lord Ermus sounds like a singular man.':
        'İlginç. Lort Ermus alışılmadık bir adama benziyor.',
    "Isn't it? I'm sure some take coin from the credulous, and some perhaps just know their herbs, but a true hedge witch has the talent.":
        'Değil mi ama? Eminim kimileri saflardan para koparır, kimileri de sadece otları bilir; ama gerçek bir köy cadısında yetenek vardır.',
    'It does seem odd.':
        'Tuhaf görünüyor.',
    "It doesn't matter, I must leave.":
        'Fark etmez, gitmem gerek.',
    "It doesn't take much. We can look for some weapons.":
        'Çok bir şey gerekmez. Silah arayabiliriz.',
    'It happened again?':
        'Yine mi oldu?',
    'It is good to be inquisitive.':
        'Meraklı olmak iyidir.',
    'It is the only way forward.':
        'İlerlemenin tek yolu bu.',
    'It must be bad.':
        'Kötü olmalı.',
    "It seems I can't remember even my own name, but you can call me {Actor[1].Name}.":
        'Görünüşe göre adımı bile hatırlamıyorum, ama bana {Actor[1].Name} diyebilirsin.',
    'It seems needlessly cruel.':
        'Gereksiz bir zulüm gibi.',
    'It seems to me that you are more than a little curious.':
        'Bana kalırsa merakın az buz değil.',
    "It sounds strange to me, but it's the only thing I seem to remember.":
        'Bana yabancı geliyor, ama hatırladığım tek şey bu.',
    "It was vicious! I'm no fighter.":
        'Azgındı! Ben dövüşçü değilim.',
    "It's admirable I guess, but still stupid.":
        'Takdire değer belki, ama yine de aptalca.',
    "It's all a bit beyond me, but thanks for explaining.":
        'Bunlar beni biraz aşar, ama açıkladığın için sağ ol.',
    "It's all the same, the hells below the underworld.":
        'Hepsi bir; yeraltı âleminin altındaki cehennemler.',
    "It's alright.":
        'Sorun değil.',
    "It's bad, I can't go on like this.":
        'Kötü, böyle devam edemem.',
    "It's just a strange thing to do. I wonder if there's more to it.":
        'Yapılması tuhaf bir şey. Acaba işin başka bir yanı var mı?',
    "It's like a door, there's nothing to fear.":
        'Bir kapı gibi, korkacak bir şey yok.',
    "It's likely that you will.":
        'Büyük olasılıkla bulursun.',
    "It's more as though I'm trying to remember something, but I can't, and it pains me.":
        'Daha çok bir şeyi hatırlamaya çalışıp başaramıyorum gibi, bu da canımı acıtıyor.',
    "It's not nonsense! This is the underworld. The dead are risen. We go into the hells!":
        'Saçmalık değil! Burası yeraltı dünyası. Ölüler dirilmiş. Cehennemlere gidiyoruz!',
    "It's not so bad. It passes quickly.":
        'O kadar kötü değil. Çabuk geçiyor.',
    'Just a little. I feel I can do more.':
        'Biraz. Daha fazlasını yapabilirim.',
    'Just a scratch.':
        'Sıyrık sadece.',
    'Just leave me be.':
        'Beni rahat bırak.',
    'Just leave me. Someone will come to help.':
        'Beni bırak. Biri yardıma gelir.',
    "Just surprised me. It's gone now.":
        'Sadece şaşırttı. Şimdi geçti.',
    'Just take whatever you want.':
        'Ne istersen al.',
    'Leave me alone!':
        'Rahat bırak!',
    'Leave, of course. Come.':
        'Gitmek tabii ki. Gel.',
    'Let me be!':
        'Bıraksana!',
    'Let me see your equipment.':
        'Teçhizatına bir bakayım.',
    'Let that be all.':
        'Bu kadarı yeter.',
    "Let us work together, we'll have a better chance of making it through this.":
        'Birlikte çalışalım; bunu atlatma şansımız daha yüksek olur.',
    "Let's go.":
        'Gidelim.',
    "Let's go. Now.":
        'Hemen gidelim.',
    "Let's not do this again. We have no choice.":
        'Bunu tekrar yapmayalım. Başka çaremiz yok.',
    "Let's see what's on the other side, we can always come back.":
        'Öbür tarafta ne var bir görelim, her zaman geri dönebiliriz.',
    "Let's start over. Who are you?":
        'Baştan alalım. Sen kimsin?',
    'Like any of this makes sense.':
        'Sanki bunun bir anlamı var.',
    'Like what?':
        'Ne gibi?',
    "Look around, clearly this wasn't put here to descend into the hells.":
        'Etrafına bak; bu apaçık cehennemlere inmek için konmamış.',
    "Look, I don't know what's happening, I don't even know who I am.":
        'Bak, neler oluyor bilmiyorum, kim olduğumu bile bilmiyorum.',
    "Look, I don't want no trouble. Just let me go.":
        'Bak, hiç sorun istemiyorum. Bırak gideyim.',
    "Looks like someone's been here.":
        'Biri buraya gelmiş anlaşılan.',
    'Looks like you got away just fine.':
        'Anlaşılan gayet iyi kurtulmuşsun.',
    "Magic? Thaumers? I think it's best you don't concern yourself with such things.":
        'Büyü mü? Tömacı mı? Bence böyle şeylere kafanı takmasan iyi olur.',
    'Man up and come with me, the dead are of little threat.':
        'Erkek ol da benimle gel, ölülerin pek zararı olmaz.',
    "Maybe because it's dangerous?":
        'Belki tehlikeli olduğu için?',
    'Maybe you should find out how you got yourself here before you mock me.':
        'Benimle alay etmeden önce buraya nasıl düştüğünü bir öğrensen iyi olur.',
    "Maybe you'll start to remember things.":
        'Belki zamanla bir şeyler aklına gelir.',
    'Me neither.\r\nWho are you?':
        'Ben de.\r\nSen kimsin?',
    'Me neither. Let us join forces and find a way out.':
        'Ben de. Güçlerimizi birleştirip bir çıkış bulalım.',
    "Might as well look around. Can't just stay here.":
        'Bari etrafa bakalım. Burada öylece duramayız.',
    "More likely you'll just find trouble.":
        'Daha çok başına iş açarsın.',
    "My Da was a soldier, he tried to teach me some, but I wasn't much for it.":
        'Babam askerdi, biraz öğretmeye çalıştı ama pek beceremedim.',
    "My Da was a soldier. Tried to teach me some, but I wasn't much for it.":
        'Babam askerdi. Biraz öğretmeye çalıştı ama pek beceremedim.',
    'My bindings are weak. I would be no match for the necromancer who did this.':
        'Bağlarım zayıf. Bunu yapan nekromantla baş edemem.',
    "My name is Derrin. I'm just a farm hand.":
        'Adım Derrin. Sıradan bir ırgatım.',
    "My name might be {Actor[1].Name}, but it sounds strange to me. I don't remember anything.":
        'Adım {Actor[1].Name} olabilir, ama bana yabancı geliyor. Hiçbir şey hatırlamıyorum.',
    "My name's Derrin. I'm just a farm hand.":
        'Benim adım Derrin. Sıradan bir ırgatım.',
    'Neither are these undead.':
        'Bu ölüler de öyle.',
    'Never mind.':
        'Boş ver.',
    'No matter, I can handle these undead.':
        'Fark etmez, bu ölülerle baş ederim.',
    "No matter. I'll be leaving now.":
        'Fark etmez. Ben gidiyorum.',
    "No matter. I'll deal with them when I get out of here.":
        'Fark etmez. Buradan çıkınca onlarla ilgilenirim.',
    "No thanks needed. We're better of together.":
        'Teşekküre gerek yok. Birlikte daha iyiyiz.',
    'No trouble, I just want to leave.':
        'Sorun çıkarmam, gitmek istiyorum.',
    'No! Go away!':
        'Hayır! Git!',
    "No! Please!\r\nI don't want any trouble.":
        'Hayır! Lütfen!\r\nHiç sorun istemiyorum.',
    "No! Please!\r\nI won't cause any trouble.":
        'Hayır! Lütfen!\r\nSorun çıkarmayacağım.',
    'No, I merely wished to see how you would react.':
        'Hayır, nasıl tepki vereceğini görmek istedim.',
    'No, but they come from the demonic planes, not a hole in the ground.':
        'Hayır, ama iblis düzlemlerinden gelir, yerdeki bir delikten değil.',
    'No, you will only slow me down.':
        'Hayır, yalnızca yavaşlatırsın.',
    'No, {Actor[0].Name}, stay.':
        'Yok {Actor[0].Name}, kal.',
    'No. And we don\'t call it magic, or "thaumers".':
        'Hayır. Ayrıca ona büyü demeyiz, "tömacı" da.',
    'No. But something is changing. I feel stronger, in some way more like myself. Whoever that is.':
        'Hayır. Ama bir şeyler değişiyor. Daha güçlü, bir bakıma daha çok kendim gibiyim. Her kimsem.',
    "No. I couldn't be. Unless perhaps I've lost more than just my memories...":
        'Hayır. Olamam. Tabii yalnızca anılarımdan fazlasını yitirmediysem...',
    'No. It is plain to me that this does not lead to the hells.':
        'Hayır. Bunun cehennemlere çıkmadığı bana apaçık.',
    'No. This place just feels familiar.':
        'Hayır. Burası bana tanıdık geliyor.',
    "No?\r\nThat's not like what you did though.":
        'Yok mu?\r\nAma senin yaptığına benzemiyor.',
    'Nor am I, but the need is upon us.':
        'Ben de değilim, ama mecburuz.',
    'Not everyone is as ignorant as you are, Derrin.':
        'Herkes senin kadar cahil değil Derrin.',
    'Not good, but I can keep going.':
        'İyi değil ama devam edebilirim.',
    "Not long. I'm confused. I can't remember much at all.":
        'Çok olmadı. Kafam karışık. Hiçbir şey hatırlamıyorum.',
    "Not much I hope.\r\nGood you're feeling stronger though.":
        'Umarım fazla değildir.\r\nYine de güçlü hissetmen iyi.',
    'Not really, she served at the Fallen Oak. We talked a few times.':
        "Pek sayılmaz, Devrik Meşe'de hizmet ederdi. Birkaç kez konuştuk.",
    "Not the same. The hells don't even make sense.":
        'Aynı şey değil. Cehennemlerde mantık bile yok.',
    "Nothing at all? That must feel right strange. I'd be scared I think.":
        'Hiç mi hiç? Çok tuhaf bir his olmalı. Ben olsam korkardım herhâlde.',
    "Nothing so stupid, I'm sure. But enough of this.":
        'Bu kadar aptalca değildir, eminim. Yeter artık.',
    'Nothing. Just a headache.':
        'Yok bir şey. Baş ağrısı.',
    'Nothing. Just confused. Where are we?':
        'Bir şey yok. Şaşkınım. Neredeyiz?',
    "Now you're saying demons aren't real?":
        'Şimdi de iblisler yok mu diyorsun?',
    'Of course it is.':
        'Elbette öyle.',
    'Of course.':
        'Elbette.',
    'Of course. I wish you luck.':
        'Elbette. Şans dilerim.',
    'Of course. They are weak and clumsy.':
        'Elbette. Zayıf ve beceriksizler.',
    "Oh I sure don't want to!":
        'Hem de hiç istemiyorum!',
    'Oh well.':
        'Neyse.',
    "Oh, I don't like this.\r\nPlease let's leave this place.":
        'Ah, bu hoşuma gitmedi.\r\nLütfen buradan gidelim.',
    "Oh, I'm not the first I don't think, but the others didn't do too good either.":
        'Sanmam ki ilk ben olayım, ama ötekilerin de pek işi rast gitmemiş.',
    'Oh. Alright then.\r\nGood luck.':
        'Ha. Peki öyleyse.\r\nBol şans.',
    'Oh. Alright.':
        'Ha. Peki.',
    'Old ruins, necromancy and strange ancient things. The rest is fancy.':
        'Eski harabeler, nekromantlık ve tuhaf kadim şeyler. Gerisi hayal.',
    'One of them chased me!':
        'Birisi beni kovaladı!',
    "One of them chased me. I'll die if I stay here, maybe we can get out together.":
        'İçlerinden biri beni kovaladı. Burada kalırsam ölürüm, belki birlikte çıkarız.',
    'Only members of the order are thaumaturges.':
        'Yalnızca tarikat üyeleri tömaturjisttir.',
    'Or anything else. That name sounds strange to me now.':
        'Ya da başka bir şeyi. O ad şimdi bana garip geliyor.',
    'Our odds will be better If we go together.':
        'Birlikte gidersek şansımız daha iyi olur.',
    "People like healers alright, but don't like tinkering with their heads.":
        'İnsanlar şifacıları sever, ama kafalarıyla oynanmasını sevmez.',
    'Perhaps in time I will remember.':
        'Belki zamanla hatırlarım.',
    'Perhaps not.':
        'Belki olmaz.',
    'Perhaps they had other reasons. What is this place?':
        'Belki başka nedenleri vardı. Burası neresi?',
    'Perhaps.\r\nWhat is this place?':
        'Belki.\r\nBurası neresi?',
    "Perhaps. I had a note, saying there's a way out, I intend to find it.":
        'Belki. Çıkış olduğunu yazan bir not vardı; bulmaya niyetliyim.',
    "Please don't hurt me.":
        'Lütfen canımı yakma.',
    'Please!':
        'Lütfen!',
    'Please, help me leave this place.':
        'Lütfen buradan çıkmama yardım et.',
    'Please, let me be.':
        'Lütfen, rahat ver.',
    'Please, take me with you!':
        'Lütfen, beni de götür!',
    "Please. I don't want no trouble.":
        'Lütfen. Hiç sorun istemiyorum.',
    "Please? I'll keep up, I'll do whatever you ask.":
        'Ne olur? Ayak uydururum, ne dersen yaparım.',
    'Reckon they got some idea.':
        'Bir bildikleri vardır.',
    'Reckon you got thrown in like me, hit your noggin. Heard that can forget you stuff.':
        'Sanırım seni de benim gibi attılar, kafanı çarptın. Öyle olunca insan unuturmuş.',
    "Religious claptrap. There's no such thing as the hells, this is just a means of travel.":
        'Dinî safsata. Cehennem diye bir şey yok; bu sadece bir yolculuk aracı.',
    "Right, let's get you ouf of here so you can make more bad decisions.":
        'Peki, seni buradan bir çıkaralım da daha çok kötü karar verebilesin.',
    'Right.\r\nSorry I asked.':
        'Peki.\r\nSormaz olaydım.',
    'Right. Sorry for all the asking.':
        'Peki. Çok sordum, kusura bakma.',
    "Right. That's why they're not liked much.":
        'Doğru. Bu yüzden pek sevilmezler.',
    'Seems the gods are against me today.':
        'Anlaşılan tanrılar bugün bana karşı.',
    "Shaper. Think I heard that before. Didn't know what it was.\r\nSorry for all the asking, always been a bit curious.":
        'Şekillendirici. Duymuştum galiba. Ne olduğunu bilmezdim.\r\nBunca soru sorduğum için kusura bakma, meraklıyımdır.',
    "She didn't look too good, I think you could do better.":
        'Pek iyi görünmüyordu, bence daha iyisini bulurdun.',
    'So be it.':
        'Pekâlâ.',
    'So be it. I wish you luck then.':
        'Öyle olsun. Sana şans dilerim.',
    "So if you can't even remember who you are, how do you know all this stuff?":
        'Peki kim olduğunu bile hatırlamıyorsan, bütün bunları nereden biliyorsun?',
    'So that you would not recognise them?':
        'Onları tanımayasın diye mi?',
    "So we're under ground? We should leave.":
        'Demek yerin altındayız? Gitmeliyiz.',
    'So what are we to do?':
        'Peki ne yapacağız?',
    "So who are you really? I'm not sure I understand.":
        'Peki sen gerçekte kimsin? Anladığımı sanmıyorum.',
    "So you can't make a link that don't break?":
        'Yani kopmayan bir bağ kuramıyor musun?',
    "So you're a coward.":
        'Demek korkaksın.',
    "So you're a spy? ":
        'Demek casussun? ',
    "So you're no longer scared?":
        'Demek artık korkmuyorsun?',
    'Some may need dealing with.':
        'Bazılarını halletmek gerek.',
    'Some may not take kindly to your ignorance.':
        'Bazıları cahilliğini hoş karşılamayabilir.',
    'Some will seek such "tinkering", but I will concede that point.':
        'Kimileri böyle bir "oynamayı" arar, ama bu noktada haklısın.',
    'Someone other than me?':
        'Benden başka biri mi?',
    'Someone with the talent would be called a shaper of bindings. Or just "shaper".':
        'Yeteneği olan birine bağ şekillendiricisi denir. Ya da kısaca "şekillendirici".',
    "Sometimes I think I remember something, but it's confused, like a dream. And I'm not really me. I can't explain it.":
        'Bazen bir şey hatırladığımı sanıyorum, ama karışık, rüya gibi. Ve o kişi tam olarak ben değilim. Anlatamıyorum.',
    "Sorry! I just don't know.":
        'Kusura bakma! Bilmiyorum.',
    "Sorry, I didn't mean to. I'm very confused.":
        'Üzgünüm, istemeden oldu. Kafam çok karışık.',
    "Sorry, I don't know what came over me.\r\nI need to leave this place.":
        'Özür dilerim, bana ne olduğunu bilmiyorum.\r\nBuradan gitmem gerek.',
    'Sorry, I will leave you alone.':
        'Üzgünüm, seni rahat bırakayım.',
    "Sorry, I'm confused.":
        'Pardon, sersemledim.',
    "Sorry, I'm confused. I don't even remember my own name.":
        'Kusura bakma, kafam karışık. Adımı bile hatırlamıyorum.',
    "Sorry. I'm just curious.":
        'Affedersin. Meraklıyım.',
    'Sounds like you could use some help. Come with me.':
        'Yardıma ihtiyacın var gibi. Benimle gel.',
    'Still nothing. I feel as though I should, but my mind goes blank.':
        'Hâlâ hiçbir şey. Hatırlamam gerekiyor gibi, ama zihnim bomboş.',
    'Still, you must see my meaning.':
        'Yine de ne dediğimi anlıyorsun.',
    'Stop!':
        'Dur!',
    'Superstitions are not knowledge.':
        'Batıl inanç bilgi değildir.',
    'Sure, let me know if you see anything useful.':
        'Tabii, işe yarar bir şey görürsen söyle.',
    "Sure, this is normal stuff people know.\r\nYou're an arse.":
        'Tabii, bunlar herkesin bildiği şeyler işte.\r\nPisliksin.',
    'Sure.':
        'Olur.',
    'Take me with you!':
        'Beni de götür!',
    "Take me with you, I won't make it on my own!":
        'Beni de götür, tek başıma kurtulamam!',
    'Thank you.':
        'Sağ ol.',
    'Thank you.\r\nMy name is Derrin.':
        'Teşekkür ederim.\r\nAdım Derrin.',
    'That dead one, I knew her. It was Marlia.\r\nFor a moment I thought she recognised me too.':
        "Şu ölü, onu tanıyordum. Marlia'ydı.\r\nBir an beni de tanıdığını sandım.",
    "That doesn't sound right. ":
        'Bu kulağa doğru gelmiyor. ',
    'That hurt.':
        'Bu acıttı.',
    'That is if you can make it out alive.':
        'Tabii buradan sağ çıkabilirsen.',
    'That makes two of us. Together we should have a fighting chance.':
        'İkimiz de öyleyiz. Birlikte bir şansımız olur.',
    'That may be so.':
        'Öyle olabilir.',
    'That may well be.\r\nWe should leave this place.':
        'Pekâlâ öyle olabilir.\r\nBuradan gitmeliyiz.',
    'That must be a portal. A doorway to another place.':
        'Bu bir geçit olmalı. Başka bir yere açılan kapı.',
    'That seems cruel.':
        'Zalimce, doğrusu.',
    'That seems odd. Why would they do that?':
        'Tuhaf görünüyor. Bunu neden yapsınlar?',
    'That sounds like a lonely and difficult life.':
        'Yalnız ve zor bir hayata benziyor.',
    'That sounds rough.':
        'Zor bir durum.',
    "That would be a binding, and that's not how it works. You can't just create light or a force, it must be borrowed from somewhere.\r\nThis requires great concentration, and as soon you stop renewing the link, it breaks.":
        'O bir bağ olurdu ve işleyişi öyle değil. Işığı ya da kuvveti yoktan var edemezsin, bir yerden ödünç alınmalı.\r\nBu büyük bir yoğunlaşma ister ve bağı tazelemeyi bıraktığın an kopar.',
    "That's a clever question. It's quite different, not impossible, but I didn't think it could be done. The dead control their bodies you see? Not the necromancer.":
        'Zekice bir soru. Bu epey farklı, imkânsız değil, ama yapılabileceğini düşünmezdim. Bedenlerini ölüler denetliyor, anlıyor musun? Nekromant değil.',
    "That's all I ask.":
        'Tek istediğim bu.',
    "That's all I know. This place is scary.":
        'Bildiğim bu kadar. Burası korkunç.',
    "That's different. Oh, I can't explain this to you, it's too complicated.":
        'O başka. Ah, bunu sana anlatamam, fazla karmaşık.',
    "That's good I guess, but keep your wits about you.":
        'İyi sanırım, ama gözünü dört aç.',
    "That's good, I suppose.":
        'İyi sanırım.',
    "That's no excuse!":
        'Mazeret değil bu!',
    "That's not funny!\r\nYou're going in first.":
        'Hiç komik değil!\r\nİlk sen gireceksin.',
    "That's not just a trick!":
        'Bu sadece numara değil!',
    "That's not what I meant.\r\nI just have doubts.":
        'Onu demek istemedim.\r\nSadece kuşkularım var.',
    'That... That was Marlia!':
        "O... O Marlia'ydı!",
    "The Order of Thaumaturges. It's not like every dullard with a trick is a thaumaturge.":
        'Tömaturjistler Tarikatı. Eline üç beş numara geçen her budala tömaturjist sayılmaz.',
    'The dangers we face have naught to do with your superstitions.':
        'Karşılaştığımız tehlikelerin batıl inançlarınla ilgisi yok.',
    "The gods won't decide my fate. I'm leaving this place.":
        'Kaderime tanrılar karar vermeyecek. Buradan gidiyorum.',
    'The order?':
        'Tarikat?',
    'The planes have open skies, if the demonologists are to be believed.':
        'İblisbilimcilere inanacaksak, o düzlemlerin gökyüzü açıktır.',
    "Then it's time to go back.":
        'Öyleyse geri dönme vakti.',
    'Then leave.':
        'Git madem.',
    'There are ancient, and forbidden, texts that talk of such things.':
        'Böyle şeylerden söz eden kadim ve yasaklı metinler var.',
    'There has to be, and nearby. They must be sustained by one.':
        'Olmalı, hem de yakında. Onları birinin ayakta tutması şart.',
    'There may be some truth to that, but this is no gateway to hell.':
        'Bunda gerçek payı olabilir, ama burası cehennem kapısı değil.',
    'There may be something to it.':
        'Bunda bir şey olabilir.',
    "There must be another way out. I'm sure of it.":
        'Başka bir çıkış olmalı. Bundan eminim.',
    "There's a necromancer too?":
        'Bir de nekromant mı var?',
    "There's a necromancer too?!":
        'Bir de nekromant mı var?!',
    "There's another exit. I'm sure of it.":
        'Başka bir çıkış var. Bundan eminim.',
    "There's dead ones everywhere!":
        'Her yer ölü dolu!',
    "There's dead ones everywhere.":
        'Her yer ölü dolu.',
    "There's dead ones everywhere. It's too dangerous.":
        'Her yer ölü dolu. Fazla tehlikeli.',
    "There's no such thing as demons.":
        'İblis diye bir şey yok.',
    "There's others here. They're dead, but like, still alive.":
        'Burada başkaları var. Ölüler, ama hani, hâlâ canlı gibi.',
    'These lamps, are they magic?':
        'Bu lambalar büyü mü?',
    "They are not much of a threat. Let's go.":
        'Pek bir tehdit sayılmazlar. Gidelim.',
    "They don't seem very aggressive, I will try to avoid them.":
        'Pek saldırgan görünmüyorlar, onlardan kaçınmaya çalışırım.',
    "They're not much trouble. Just stay clear of them.":
        'Pek sorun çıkarmazlar. Sadece onlardan uzak dur.',
    "They're not! One of them chased me!":
        'Değiller ki! Biri beni kovaladı!',
    'This has been here a very long time, yet there are no demons.':
        'Burası çok uzun zamandır duruyor, yine de ortada iblis yok.',
    "This is the underworld! The ancients went places they shouldn't have. Everyone knows this!":
        'Burası yeraltı dünyası! Kadimler gitmemeleri gereken yerlere gitti. Bunu herkes bilir!',
    'Those who can heal the body can just as well do great harm.':
        'Bedeni iyileştirebilenler, pekâlâ büyük zarar da verebilir.',
    'Through here might well be our exit.':
        'Çıkışımız buradan olabilir.',
    'Thrown in where?':
        'Nereye atıldın?',
    'Thrown in?':
        'Atıldın?',
    'Together we can make it.':
        'Birlikte başarabiliriz.',
    "True enough. Come with me, I'll protect you.":
        'Doğru diyorsun. Benimle gel, seni korurum.',
    'Under the circumstances.':
        'Koşullar düşünülürse.',
    'Very well, you may follow. But you must take care of yourself.':
        'Pekâlâ, gelebilirsin. Ama kendine kendin bakacaksın.',
    'Wait for me here.':
        'Sen burada bekle.',
    'Wait, I mean you no harm.':
        'Dur, sana zarar vermem.',
    'Wait.':
        'Dur.',
    'Wait. I mean you no harm.':
        'Dur. Sana zarar vermem.',
    'We can handle these undead between us.':
        'Bu ölülerin ikimiz hakkından geliriz.',
    "We can't be sure, and yet we must act.":
        'Emin olamayız ama harekete geçmeliyiz.',
    "We can't just stand around and wait to die. We must search for an exit.":
        'Öylece durup ölümü bekleyemeyiz. Bir çıkış aramalıyız.',
    "We don't know what clever thing you did to get stuck here.":
        'Buraya sıkışmak için ne akıllıca iş yaptın, bilmiyoruz.',
    "We just didn't see any.":
        'Sadece hiç görmedik.',
    'We make a good team then.':
        'Demek iyi bir ekip olduk.',
    'We need to get out of here.':
        'Buradan çıkmamız gerek.',
    'We shall see.':
        'Göreceğiz.',
    'We should focus on getting out of here.':
        'Buradan çıkmaya odaklanmalıyız.',
    'We should look around. My Da would say even a good shirt can save your skin.':
        'Etrafa bakmalıyız. Babam derdi ki iyi bir gömlek bile canını kurtarabilir.',
    'We should look around. My Da would say just a good shirt can save your skin.':
        'Etrafa bakmalıyız. Babam derdi ki sırf iyi bir gömlek canını kurtarabilir.',
    "We shouldn't be here. It's not right.":
        'Burada olmamalıyız. Doğru değil.',
    "We'll get by. Let's be on our way.":
        'İdare ederiz. Yola koyulalım.',
    "We'll just have to look around.":
        'Etrafa bakmaktan başka yol yok.',
    "We'll need to be watchful of them when we leave.":
        'Giderken onlara karşı tetikte olmalıyız.',
    "We're not dead yet. We may fair better still.":
        'Daha ölmedik. İşimiz yine de rast gidebilir.',
    "We're under ground, and there is necromancy at work. Don't let your imagination carry you too far.":
        'Yerin altındayız ve işin içinde nekromantlık var. Hayal gücünü fazla uzağa götürme.',
    "We're under ground. I was thrown down by bandits.\r\nReckon you did too and hit your head.":
        'Yerin altındayız. Beni haydutlar aşağı attı.\r\nSanırım sen de öyle düşüp kafanı çarptın.',
    'We?\r\nSo you are a thaumer!':
        'Biz mi?\r\nDemek tömacısın!',
    "Well Derrin, I'm not sure I even remember my own name.\r\nBut you can call me {Actor[1].Name}.":
        'Şey Derrin, kendi adımı bile hatırlamıyorum galiba.\r\nAma bana {Actor[1].Name} diyebilirsin.',
    "Well, I don't plan on staying here much longer.":
        'Şey, burada daha fazla kalmaya niyetim yok.',
    'Well, I fancy our chances more now.':
        'Şey, şansımız artık daha iyi bence.',
    "Well, I hadn't given it thought. But look!\r\nWe are deep below ground, the dead are risen and there are such things as this!":
        'Şey, bunu düşünmemiştim. Ama baksana!\r\nYerin çok altındayız, ölüler dirilmiş ve böyle şeyler var!',
    'Well, I wanted to help, so I tried to find the bandits.':
        'Şey, yardım etmek istedim, haydutları bulmaya çalıştım.',
    'Well, I will look for another exit.':
        'Peki, ben başka çıkış arayacağım.',
    'Well, good luck with that.':
        'Peki, kolay gelsin.',
    "Well, it might be {Actor[1].Name}, but I don't really remember anything at all.":
        'Şey, {Actor[1].Name} olabilir, ama aslında hiçbir şey hatırlamıyorum.',
    "Well, it seems they wanted to be rid of you. Perhaps they didn't have the stomach for it.":
        'Peki, görünüşe göre senden kurtulmak istemişler. Belki de gözleri kesmedi.',
    "Well, let's be on our way.":
        'Peki, yola koyulalım.',
    "Well, let's get out of here.":
        'Peki, hadi çıkalım buradan.',
    "Well, let's get you out of here.":
        'Pekâlâ, seni buradan çıkaralım.',
    'Well, probably.':
        'Eh, muhtemelen.',
    "Well, she won't be doing that anymore.":
        'Şey, artık bunu yapmayacak.',
    'Well, thanks for clearing that up. I have better measure of you now.':
        'Peki, açıkladığın için sağ ol. Seni artık daha iyi tartabiliyorum.',
    "Well, that's me.":
        'İşte ben buyum.',
    "Well, that's not a healer then is it?":
        'E, o zaman şifacı sayılmaz, değil mi?',
    "Well, they probably didn't expect us to make it out alive, but I'll prove them wrong.":
        'Şey, herhâlde sağ çıkacağımızı beklemediler, ama yanıldıklarını göstereceğim.',
    'Well, time to find a way out.':
        'Peki, bir çıkış bulma vakti.',
    'Well, we should leave.':
        'Peki, gitmeliyiz.',
    "Well, yeah, but I thought if you can do magics you're a thaumer.":
        'Şey, evet, ama büyü yapabiliyorsan tömacısın sanıyordum.',
    "Well, yes, but I don't have a better answer. Perhaps it is a more clever mechanism.":
        'Şey, evet, ama daha iyi bir yanıtım yok. Belki daha zekice bir düzenektir.',
    "Well, you keep hiding. I'm going to find a way out of here.":
        'Peki, saklanmaya devam et. Ben buradan bir çıkış bulacağım.',
    "Well...\r\nI don't know.":
        'Şey...\r\nBilmiyorum.',
    'What a horrible thing to say!':
        'Ne korkunç bir laf!',
    'What a peculiar arrangement. Thanks for explaining, I have a better measure of you now.':
        'Ne tuhaf bir düzen. Açıkladığın için sağ ol, seni artık daha iyi tartabiliyorum.',
    'What about me?':
        'Ya ben?',
    'What about the dead ones?':
        'Ya ölüler?',
    'What about you?':
        'Ya sen?',
    'What are you doing here?':
        'Burada ne yapıyorsun?',
    'What can a necromancer do then?':
        'Peki nekromant neler yapabilir?',
    'What do you mean by magic?':
        'Büyüyle ne kastediyorsun?',
    'What do you mean?':
        'Ne demek istedin?',
    "What if we can't? What if we die?":
        'Ya başaramazsak? Ya ölürsek?',
    'What imminent peril do you imagine now?':
        'Şimdi hangi tehlikeyi hayal ediyorsun?',
    'What was it of?':
        'Neye dairdi?',
    'What! Why?':
        'Ne! Neden?',
    'What!? Why?':
        'Ne!? Neden?',
    "What's that strange smell?":
        'Bu tuhaf koku da ne?',
    "What's that?!":
        'O da ne?!',
    "What's wrong with you?":
        'Senin neyin var?',
    "What's wrong?":
        'Ne oldu?',
    "What's your name?":
        'Adın ne?',
    'What?':
        'Ne?',
    'What? How long have you been here?':
        'Ne? Ne zamandır buradasın?',
    'What? Why would you think that?':
        'Ne? Bunu neden düşünesin ki?',
    "What? You're vile! It wasn't like that, I just knew her is all.":
        'Ne? İğrençsin! Öyle bir şey değildi, sadece tanıyordum işte.',
    'Whatever the case, I must leave this place.':
        'Her hâlükârda buradan gitmem gerek.',
    'Where we are is just not what you think it is.':
        'Bulunduğumuz yer, sandığın şey değil.',
    'Who are you?':
        'Sen kimsin?',
    'Who threw you in?':
        'Seni kim attı?',
    'Why are we going deeper?\r\nI thought we were trying to get out.':
        'Neden daha da aşağı iniyoruz?\r\nÇıkmaya çalışıyoruz sanıyordum.',
    'Why are you so scared? Find your courage.':
        'Niye böyle korkuyorsun? Cesaretini topla.',
    'Why not just kill you?':
        'Neden öldürmediler ki?',
    'Why would bandits throw you in here?':
        'Haydutlar seni neden buraya atsın?',
    'Why would they do that?':
        'Bunu neden yapsınlar?',
    'With you? No.':
        'Seninle? Yok.',
    "Worried more like!\r\nBut I guess I am more curious than I'm wise.":
        'Daha çok endişeli desene!\r\nAma galiba aklımdan çok merakım var.',
    'Would you call a hedge witch a "thaumer"?':
        'Bir köy cadısına "tömacı" der miydin?',
    'Yeah, clearly it was not.':
        'Evet, belli ki değilmiş.',
    "Yeah, it's just similar is all.":
        'Evet, sadece benziyor işte.',
    'Yeah, not my best idea. But we lost so many, I wanted to do something.':
        'Evet, iyi fikir değildi. Ama çok kayıp verdik, bir şey yapmak istedim.',
    "Yeah, you're right.":
        'Evet, haklısın.',
    "Yeah. It's nothing, don't worry about.":
        'Evet. Bir şey değil, dert etme.',
    'Yeah. The same feeling.':
        'Evet. Aynı his.',
    'Yeah?\r\nThank you!':
        'Sahi mi?\r\nSağ ol!',
    "Yes, I guess he is. I'm glad for it.":
        'Evet, galiba öyle. Buna seviniyorum.',
    'Yes, we could use some weapons too.':
        'Evet, biraz silah da işimize yarar.',
    'Yes, we may be able to help each other.':
        'Evet, birbirimize yardım edebiliriz.',
    'Yes.':
        'Evet',
    "Yes. I was thinking to try on my own, but I'm scared If I'm honest.":
        'Evet. Tek başıma denemeyi düşünüyordum, ama doğrusu korkuyorum.',
    'Yes. Just let me be.':
        'Evet. Rahat bırak.',
    'You and Lord Ermus are friends? That seems odd.':
        'Sen ve Lort Ermus dost musunuz? Bu tuhaf geldi.',
    'You are right. And a mind shaper is not a necromancer.':
        'Haklısın. Zihin şekillendirici de nekromant değildir.',
    "You are weak, don't get overconfident.":
        'Zayıfsın, fazla güvenme kendine.',
    'You attacked me!':
        'Bana saldırdın!',
    'You better toughen up and ignore it, might not be the last one you recognise.':
        'Sertleşip aldırmasan iyi olur, tanıdığın son kişi olmayabilir.',
    "You can trust me Derrin. Let's get out of here.":
        'Bana güvenebilirsin Derrin. Hadi çıkalım artık.',
    "You can't remember your name?":
        'Adını hatırlamıyor musun?',
    "You can't stay here. I'm sure we can find a way out.":
        'Burada kalamazsın. Eminim bir çıkış bulabiliriz.',
    'You can?':
        'Sahi mi?',
    'You could come with me.':
        'Benimle gelebilirsin.',
    "You don't know who you are?":
        'Kim olduğunu bilmiyorsun?',
    "You don't understand what I'm going through.":
        'Neler yaşadığımı anlamıyorsun.',
    'You just asked me.':
        'Az önce sordun.',
    'You know, it makes me think of when you uncover an ant nest, when working the soil.':
        'Biliyor musun, bu bana toprağı işlerken bir karınca yuvasını açmayı hatırlatıyor.',
    'You know, the stuff thaumers do.':
        'Hani tömacıların yaptığı şeyler.',
    'You may join me, if you wish.':
        'İstersen bana katılabilirsin.',
    'You must die.':
        'Ölmelisin.',
    'You must know of the Order of Thaumaturges!':
        "Tömaturjistler Tarikatı'nı biliyorsundur!",
    "You need me {Actor[0].Name}. You can't survive on your own.":
        'Bana ihtiyacın var {Actor[0].Name}. Yalnız kurtulamazsın.',
    'You pretend you are ignorant, but sometimes you forget. You are too clever and literate.':
        'Cahil numarası yapıyorsun, ama bazen unutuyorsun. Fazla zeki ve okumuşsun.',
    "You pretend you don't know!\r\nIt is plain. Tell me it isn't so.":
        'Bilmiyormuş gibi yapıyorsun!\r\nApaçık. Öyle değilse söyle.',
    'You really think someone will come find you?':
        'Birinin gelip seni bulacağını mı sanıyorsun?',
    'You refuse my friendship? Fuck you then.':
        'Dostluğumu reddettin demek? Siktir git.',
    "You see? I didn't do nothing!":
        'Gördün mü? Bir şey yapmadım!',
    'You speak of the underworld, but It is just an ancient place, below the ground.':
        'Yeraltı dünyasından söz ediyorsun, oysa burası kadim bir yer, yerin altında.',
    "You still don't remember anything at all?":
        'Hâlâ hiçbir şey hatırlamıyor musun?',
    'You think?':
        'Öyle mi?',
    "You won't change my mind.":
        'Fikrimi değiştiremezsin.',
    "You'll regret refusing my help.":
        'Yardımımı teptiğine yanarsın.',
    "You're a thaumer!":
        'Sen tömacısın!',
    "You're just pretending like you don't know where we are.":
        'Nerede olduğumuzu bilmiyormuş gibi yapıyorsun sadece.',
    "You're just saying all that so I won't be feared.":
        'Bütün bunları korkmayayım diye söylüyorsun.',
    "You're lying!":
        'Yalancısın!',
    "You're mad!\r\nWe're not doing that!":
        'Sen delisin!\r\nBunu yapmıyoruz!',
    "You're mad! Just let me go.":
        'Sen delisin! Bırak gideyim.',
    "You're not listening!\r\nThis isn't just some place.":
        'Beni dinlemiyorsun!\r\nBurası sıradan bir yer değil.',
    "You're right. I don't need to hide this from you.":
        'Haklısın. Bunu senden gizlememe gerek yok.',
    "You're scaring me. Please let me be.":
        'Korkutuyorsun. Lütfen rahat bırak.',
    "You're talking about things you don't understand.":
        'Anlamadığın şeyler hakkında konuşuyorsun.',
    '{Actor[0].Name}, I need your help. Please.':
        '{Actor[0].Name}, yardımın gerek. Lütfen.',
    '{Actor[0].Name}, we need to stick together.':
        '{Actor[0].Name}, bir arada kalmalıyız.',
    '{Actor[1].Name} perhaps? It sounds strange to me now.':
        'Belki {Actor[1].Name}? Şimdi bana yabancı geliyor.',
    "{Actor[1].Name}? I'm not sure even of that.":
        '{Actor[1].Name} mi? Ondan bile emin olamam.',
    "Derrin. I'm\x85 {Actor[1].Name}, I think.":
        'Derrin. Ben… {Actor[1].Name}, sanırım.',
    'Well met Derrin. I go by\x85 {Actor[1].Name}, I think.':
        'Memnun oldum Derrin. Ben… {Actor[1].Name}, sanırım.',
    "I'm\x85 Just a farm hand. Name's Derrin.":
        'Ben… Sıradan bir ırgat. Adım Derrin.',
    "I\x85 don't recall.":
        'Ben… hatırlamam.',
    "Drop the façade. I'm the only friend you have here.":
        'Bu numarayı bırak. Burada tek dostun benim.',
}

NARRATOR = {
    '\tHere lies the body of Corlian.\r\n\r\n\tA flood of memories overcomes you, and you understand that Corlian is not truly dead, but resides somewhere inside you, sharing your consciousness with your former self.\r\n\r\n\tA conflict rages inside you, you feel you must choose which is your true self, or perhaps to make peace with this duality.':
        "\tBurada Corlian'ın bedeni yatıyor.\r\n\r\n\tÜzerine bir anı seli çöküyor ve anlıyorsun ki Corlian gerçekten ölmedi; içinde bir yerde duruyor, bilincini eski benliğinle paylaşıyor.\r\n\r\n\tİçinde bir çatışma kaynıyor; gerçek benliğinin hangisi olduğunu seçmen, ya da belki bu ikilikle barışman gerektiğini hissediyorsun.",
    'I am {Actor[1].Name}, master of forces.':
        'Ben {Actor[1].Name}, kuvvet efendisi.',
    'I am Corlian, master of minds.':
        'Ben Corlian, zihin efendisi.',
    'I am neither, and I am both.':
        'Ne biri ne öteki; ikisiyim.',
    'You feel strongly attuned to forces and the motions of objects.':
        'Kuvvetlere ve nesnelerin devinimine güçlü bir uyum duyuyorsun.',
    'You feel your connection to the minds of others flow effortlessly.':
        'Başkalarının zihniyle bağının zahmetsizce aktığını hissediyorsun.',
    'You feel that control over forces and minds comes to you more easily.':
        'Kuvvet ve zihin üzerindeki denetimin kolaylaştığını hissediyorsun.',
    'Confused memories surface, but you fight them down in fear.\r\n\r\nNevertheless something was restored.':
        'Karışık anılar yüzeye çıkıyor, ama korkuyla onları bastırıyorsun.\r\n\r\nYine de bir şey geri geldi.',
    "These notes describe a raising of the dead that doesn't require a bond to be held by the necromancer.\r\n\r\nWith this knowledge revealed to you, you think you would be able to replicate these methods.":
        'Bu notlar, nekromantın bir bağ tutmasını gerektirmeyen bir ölü diriltme yöntemini anlatıyor.\r\n\r\nBu bilgi sana açıldığına göre, bu yöntemleri yineleyebileceğini düşünüyorsun.',
    "These notes describe a raising of the dead that doesn't require a bond to be held by the necromancer.\r\n\r\nYou lack the knowledge or the insight to understand how it might be done.":
        'Bu notlar, nekromantın bir bağ tutmasını gerektirmeyen bir ölü diriltme yöntemini anlatıyor.\r\n\r\nBunun nasıl yapılabileceğini anlayacak bilgiden ya da sezgiden yoksunsun.',
    "As a shaper's mind dissipates you glean some knowledge of their power.":
        'Bir şekillendiricinin zihni dağılırken gücünden bir parça öğrenirsin.',
}
