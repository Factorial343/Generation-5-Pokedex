import pygame
#pygame.init()
#window = pygame.display.set_mode((600=545))
#window.fill((245=170=245))
#r11 = pygame.transform.scale(rocpic1= (135=100))
#window.blit()
pygame.init()
window = pygame.display.set_mode((300,200))
Victini = pygame.image.load("0vic.jpg")
Snivy = pygame.image.load("1sni.jpg")
SnivyFix = pygame.transform.scale(Snivy,(237,190))
Servine = pygame.image.load("2ser.jpg")
Serperior =pygame.image.load("3ser.jpg")
Tepig = pygame.image.load("4tep.jpg")
Pignite = pygame.image.load("5pig.jpg")
Emboar = pygame.image.load("6emb.jpg")
Oshawott = pygame.image.load("7osh.jpg")
Dewott = pygame.image.load("8dew.jpg")
Samurott = pygame.image.load("9sam.jpg")
Patrat = pygame.image.load("10pat.jpg")
PatratFix = pygame.transform.scale(Patrat,(190,190))
Patrat2 = pygame.image.load("10pat2.jpg")
Patrat2Fix = pygame.transform.scale(Patrat2,(190,190))
Watchog = pygame.image.load("11wat.jpg")
Lillipup = pygame.image.load("12lil.jpg")
Herdier = pygame.image.load("13her.jpg")
Purrloin = pygame.image.load("14pur.webp")
Stoutland = pygame.image.load("14sto.jpg")
Purrlion2 = pygame.image.load("15pur.jpg")
Liepard = pygame.image.load("16lie.jpg")
Pansage = pygame.image.load("17pan.jpg")
Simisage = pygame.image.load("18simi.jpg")
Pansear = pygame.image.load("19pan.jpg")
Simisear = pygame.image.load("20simi.jpg")
Panpour = pygame.image.load("21pan.jpg")
PanpourFix = pygame.transform.scale(Panpour,(360,270))
Simipour = pygame.image.load("21simi.png")
Munna = pygame.image.load("23mun.jpg")
Musharna = pygame.image.load("24mus.jpg")
Pidove= pygame.image.load("25pid.jpg")
Tranquill= pygame.image.load("26tra.jpg")
Unfezant= pygame.image.load("27unf.jpg")
Unfezant2= pygame.image.load("27unf2.jpg")
Blitzle= pygame.image.load("28bli.jpg")
Zebstrika= pygame.image.load("29zeb.jpg")
Roggenrola= pygame.image.load("30rog.png")
Boldore= pygame.image.load("31bol.jpg")
Gigalith= pygame.image.load("32gig.jpg")
Woobat= pygame.image.load("33woo.jpg")
Swoobat=  pygame.image.load("34swo.jpg")
Drilbur= pygame.image.load("35dri.jpg")
Excadrill= pygame.image.load("36exc.jpg")
Audino= pygame.image.load("37aud.jpg")
Timburr= pygame.image.load("38tim.jpg")
Gurdurr= pygame.image.load("39gur.jpg")
Conkeldurr= pygame.image.load("40con.jpg")
Tympole= pygame.image.load("41tym.jpg")
Palpitoad= pygame.image.load("42pal.jpg")
Seismitoad= pygame.image.load("43sei.jpg")
Throh= pygame.image.load("44thr.jpg")
Sawk= pygame.image.load("45saw.jpg")
Sewaddle= pygame.image.load("46sew.jpg")
Swadloon= pygame.image.load("47swa.jpg")
Leavanny = pygame.image.load("48lea.jpg")
Venipede= pygame.image.load("49ven.jpg")
Whirlipede = pygame.image.load("50whi.jpg")
Scolipede = pygame.image.load("51sco.jpg")
Cottonee = pygame.image.load("52cot.jpg")
Whimsicott = pygame.image.load("53whi.jpg")
Petilil = pygame.image.load("54pet.jpg")
Lilligant = pygame.image.load("55lil.jpg")
Basculin = pygame.image.load("56bas.jpg")
Sandile = pygame.image.load("57san.jpg")
Krokorok = pygame.image.load("58kro.jpg")
Krookodile = pygame.image.load("59kro.jpg")
Darumaka = pygame.image.load("60dar.jpg")
Darmanitan = pygame.image.load("61dar.jpg")
Darmanitan2 = pygame.image.load("61dar2.jpg")
Maractus = pygame.image.load("63mar.jpg")
Dwebble = pygame.image.load("63dwe.jpg")
Dwebble2 = pygame.image.load("63dwe2.jpg")
Crustle = pygame.image.load("64cru.jpg")
Scraggy = pygame.image.load("65scr.jpg")
Scrafty = pygame.image.load("66scr.png")
Sigilyph = pygame.image.load("67sig.jpg")
SigilyphFix = pygame.transform.scale(Sigilyph,(321,420))
Yamask = pygame.image.load("69cof.jpg")
Cofagrigus = pygame.image.load("69cof.jpg")
Cofagrigus2 = pygame.image.load("69cof2.jpg")
Tirtouga = pygame.image.load("70tir.jpg")
Carracosta = pygame.image.load("71car.jpg")
Archen = pygame.image.load("72arc.jpg")
Archeops = pygame.image.load("73arc.jpg")
Trubbish = pygame.image.load("74tru.jpg")
Garbodor = pygame.image.load("75gar.jpg")
Zorua = pygame.image.load("76zor.jpg")
Zorua2 = pygame.image.load("76zor2.jpg")
Zorua3 = pygame.image.load("76zor3.jpg")
Zoroark = pygame.image.load("77zor.jpg")
Minccino = pygame.image.load("78min.jpg")
Cinccino = pygame.image.load("79cin.jpg")
Gothita = pygame.image.load("80got.jpg")
Gothorita = pygame.image.load("81got.jpg")
Gothitelle = pygame.image.load("82got.jpg")
Solosis= pygame.image.load("83sol.jpg")
Duosion= pygame.image.load("84duo.jpg")
Reuniclus= pygame.image.load("85reu.jpg")
Ducklett= pygame.image.load("86duc.jpg")
Swanna= pygame.image.load("87swa.jpg")
Vanillite= pygame.image.load("88van.jpg")
Vanillish=pygame.image.load("89van.jpg")
Vanilluxe=pygame.image.load("90van.jpg")
Deerling=pygame.image.load("91dee.jpg")
Deerling2=pygame.image.load("91dee2.jpg")
Sawsbuck=pygame.image.load("92saw.jpg")
Sawsbuck2=pygame.image.load("92saw2.jpg")
Sawsbuck2Fix = pygame.transform.scale(Sawsbuck2,(175,210))
Emolga= pygame.image.load("93emo.jpg")
Karrablast= pygame.image.load("94kar.jpg")
Escavalier= pygame.image.load("95esc.jpg")
Foongus= pygame.image.load("96foo.jpg")
Amoonguss=pygame.image.load("97amo.jpg")
Amoonguss2=pygame.image.load("97amo2.jpg")
Frillish=pygame.image.load("98fri.jpg")
Jellicent=pygame.image.load("99jel.jpg")
Alomomola= pygame.image.load("100alo.jpg")
Joltik= pygame.image.load("101jol.jpg")
Galvantula=pygame.image.load("102gal.jpg")
Ferroseed= pygame.image.load("103fer.jpg")
Ferrothorn= pygame.image.load("104fer.jpg")
Klink= pygame.image.load("105kli.jpg")
Klang=pygame.image.load("106kla.jpg")
Klinklang= pygame.image.load("107kli.jpg")
Tynamo= pygame.image.load("108tyn.jpg")
Eelektrik= pygame.image.load("109eel.jpg")
Eelektross= pygame.image.load("110eel.jpg")
Elgyem=pygame.image.load("111elg.jpg")
Beheeyem=pygame.image.load("112bee.jpg")
Litwick= pygame.image.load("113lit.jpg")
Lampent= pygame.image.load("114lam.jpg")
Chandelure= pygame.image.load("115cha.jpg")
Axew= pygame.image.load("116axe.jpg")
Fraxure= pygame.image.load("117fra.jpg")
Haxorus= pygame.image.load("118hax.jpg")
Haxorus2= pygame.image.load("118hax2.jpg")
Haxorus2Fix = pygame.transform.scale(Haxorus2,(216,293))
Cubchoo=pygame.image.load("119cub.jpg")
Beartic= pygame.image.load("120bea.jpg")
Cryogonal=pygame.image.load("121cry.jpg")
Shelmet= pygame.image.load("122she.jpg")
Accelgor= pygame.image.load("123acc.jpg")
Stunfisk= pygame.image.load("124stu.jpg")
Mienfoo= pygame.image.load("125mie.jpg")
Mienshao= pygame.image.load("126mie.jpg")
Druddigon= pygame.image.load("127dru.jpg")
Golett= pygame.image.load("128gol.jpg")
Golurk= pygame.image.load("129gol.jpg")
Pawniard= pygame.image.load("130paw.jpg")
Bisharp=pygame.image.load("131bis.jpg")
Bouffalant= pygame.image.load("132bou.jpg")
Rufflet= pygame.image.load("133ruf.jpg")
Braviary= pygame.image.load("134bra.jpg")
Vullaby= pygame.image.load("135vul.jpg")
Mandibuzz= pygame.image.load("136man.jpg")
Heatmor= pygame.image.load("137hea.jpg")
Durant= pygame.image.load("138dur.jpg")
Deino= pygame.image.load("139dei.jpg")
Zweilous= pygame.image.load("140zwe.jpg")
Hydreigon= pygame.image.load("141hyd.jpg")
Hydreigon2= pygame.image.load("141hyd2.png")
Larvesta= pygame.image.load("142lar.jpg")
Volcarona= pygame.image.load("143vol.jpg")
Cobalion = pygame.image.load("144cob.jpg")
Terrakion= pygame.image.load("145ter.jpg")
Virizion=pygame.image.load("146vir.jpg")
Tornadus=pygame.image.load("147tor.jpg")
Tornadus2=pygame.image.load("147tor2.jpg")
Thundurus=pygame.image.load("148thu.jpg")
Reshiram= pygame.image.load("149res.jpg")
Zekrom=pygame.image.load("150zek.jpg")
Zekrom2=pygame.image.load("150zek2.jpg")
Landorus=pygame.image.load("151lan.jpg")
Kyurem= pygame.image.load("152kyu.jpg")
KyuremFix = pygame.transform.scale(Kyurem,(241,133))
Kyurem2= pygame.image.load("152kyu2.jpg")
Kyurem3= pygame.image.load("152kyu3.png")
Keldeo= pygame.image.load("153kel.jpg")
Keldeo2= pygame.image.load("153kel2.jpg")
Meloetta= pygame.image.load("154mel.jpg")
Genesect =pygame.image.load("155gen.jpg")
