from vari import none,pre,post, t,numb, n, des, nor, wat, fir, gra, ele, fig, bug, psy, roc, gro, poi, dar, fly, ste, ice, dra, gho ,norC, watC, firC, graC, eleC, figC, bugC, psyC, rocC, groC, poiC, darC, flyC, steC, iceC, draC, ghoC,useablenums,randomnums,truerandom
from colorama import Fore, Back, Style
import random,pygame
from pictures import Victini,SnivyFix, Servine,Serperior,Tepig,Pignite,Emboar,Oshawott,Dewott,Samurott,PatratFix,Patrat2Fix,Watchog,Lillipup,Herdier,Stoutland,Purrloin,Liepard,Pansage,Simisage,Pansear, Simisear,PanpourFix,Simipour,Munna,Musharna,Pidove,Tranquill,Unfezant,Unfezant2,Blitzle,Zebstrika,Roggenrola, Boldore, Gigalith, Woobat, Swoobat, Drilbur, Excadrill,Audino,Timburr,Gurdurr,Conkeldurr,Tympole,Palpitoad,Seismitoad,Throh,Sawk,Sewaddle,Swadloon,Leavanny,Venipede,Whirlipede, Scolipede,Cottonee,Whimsicott,Petilil, Lilligant,Basculin,Sandile,Krokorok, Krookodile,Darumaka, Darmanitan,Darmanitan2, Maractus,Dwebble,Dwebble2,Crustle,Scraggy,Scrafty,SigilyphFix,Yamask,Cofagrigus,Cofagrigus2, Tirtouga, Carracosta,Archen,Archeops, Trubbish, Garbodor, Zorua,Zorua2,Zorua3, Zoroark,Minccino, Cinccino,Gothita,Gothorita,Gothitelle,Solosis,Duosion,Reuniclus,Ducklett, Swanna, Vanillite, Vanillish,Vanilluxe,Deerling,Deerling2,Sawsbuck,Sawsbuck2Fix,Emolga, Karrablast, Escavalier,Foongus,Amoonguss,Amoonguss2,Frillish,Jellicent,Alomomola, Joltik, Galvantula,Ferroseed, Ferrothorn, Klink, Klang,Klinklang, Tynamo, Eelektrik, Eelektross, Elgyem,Beheeyem,Litwick, Lampent, Chandelure, Axew, Fraxure, Haxorus,Haxorus2Fix, Cubchoo,Beartic,Cryogonal,Shelmet, Accelgor, Stunfisk, Mienfoo, Mienshao, Druddigon, Golett, Golurk, Pawniard, Bisharp,Bouffalant, Rufflet, Braviary, Vullaby, Mandibuzz, Heatmor, Durant, Deino, Zweilous, Hydreigon,Hydreigon2, Larvesta, Volcarona, Cobalion , Terrakion, Virizion,Tornadus,Tornadus2,Thundurus,Reshiram, Zekrom,Zekrom2,Landorus,KyuremFix,Kyurem2,Kyurem3, Keldeo,Keldeo2, Meloetta, Genesect
from Word import victini,snivy,servine,serperior,tepig,pignite,emboar,oshawott,dewott,samurott,patrat,watchog,lillipup,herdier,stoutland,purrloin,liepard,pansage,simisage, pansear, simisear,panpour,simipour,munna,musharna,pidove,tranquill,unfezant,blitzle,zebstrika,roggenrola, boldore, gigalith, woobat, swoobat, drilbur, excadrill,audino,timburr,gurdurr,conkeldurr,tympole,palpitoad,seismitoad,throh,sawk,sewaddle,swadloon,leavanny,venipede,whirlipede, scolipede,cottonee,whimsicott,petilil, lilligant,basculin,sandile,krokorok, krookodile,darumaka, darmanitan, maractus,dwebble,crustle,scraggy,scrafty,sigilyph,yamask,cofagrigus, tirtouga, carracosta,archen,archeops, trubbish, garbodor, zorua, zoroark,minccino, cinccino,gothita,gothorita,gothitelle,solosis,duosion,reuniclus,ducklett, swanna, vanillite, vanillish,vanilluxe,deerling,sawsbuck,emolga, karrablast, escavalier,foongus,amoonguss,frillish,jellicent,alomomola, joltik, galvantula,ferroseed, ferrothorn, klink, klang,klinklang, tynamo, eelektrik, eelektross, elgyem,beheeyem,litwick, lampent, chandelure, axew, fraxure, haxorus, cubchoo,beartic,cryogonal,shelmet, accelgor, stunfisk, mienfoo, mienshao, druddigon, golett, golurk, pawniard, bisharp,bouffalant, rufflet, braviary, vullaby, mandibuzz, heatmor, durant, deino, zweilous, hydreigon, larvesta, volcarona, cobalion , terrakion, virizion,tornadus,thundurus,reshiram, zekrom,landorus,kyurem, keldeo, meloetta, genesect

class Pokemon():
  def __init__(self, name, num, color,before,after,ex) :
    self.name = name
    self.color = color
    self.num = num
    self.before = before
    self.after = after
    self.ex = ex

  def info(param):  
    #result only exists in this class so I have to change the color of its output in here otherwise it wont work
    result = {n: param.name, numb :param.num, t: param.color, pre: param.before, post:param.after,des:param.ex}

    if psy+"/" in result.get(t):
      print(Back.RED, end = "")
      print(Style.BRIGHT, end = "")
    elif wat+"/" in result.get(t):
      print(Fore.CYAN, end = "")
      
    elif gra+"/" in result.get(t):
      print(Back.GREEN, end = "")
    elif bug+"/" in result.get(t):
      print(Fore.GREEN, end = "")
    elif fir+"/" in result.get(t):
      print(Back.RED, end = "")
      print(Fore.BLACK, end = "")
      
    elif fig+"/" in result.get(t):
      print(Fore.RED, end = "")
      print(Style.DIM, end = "")
    elif ele+"/" in result.get(t):
      print(Back.YELLOW, end = "")
      print(Style.BRIGHT, end = "")
    elif roc+"/" in result.get(t):
      print(Fore.YELLOW, end = "")
      print(Style.DIM, end = "")
    elif gro+"/" in result.get(t):
      print(Fore.YELLOW, end = "")
    elif ice+"/" in result.get(t):
      print(Back.CYAN, end = "")
      print(Style.BRIGHT, end = "")
    elif poi+"/" in result.get(t):
      print(Fore.MAGENTA, end = "")
      print(Style.BRIGHT, end = "")
    elif dar+"/" in result.get(t):
      print(Back.BLACK, end = "")
    elif ste+"/" in result.get(t):
      print(Fore.WHITE, end = "")
      print(Style.DIM, end = "")
    elif gho+"/" in result.get(t):
       print(Back.MAGENTA, end = "")
       print(Style.DIM, end = "")
       
    elif fly in result.get(t) or nor+"/"+fly in result.get(t):
      print(Fore.BLUE, end = "")
      print(Style.BRIGHT, end = "")
    elif nor+"/" in result.get(t):
      print(Back.WHITE, end = "")
      print(Fore.BLACK, end = "")
    elif psy in result.get(t):
      print(Back.RED, end = "")
      print(Style.BRIGHT, end = "")
    elif wat in result.get(t):
      print(Fore.CYAN, end = "")
      print(Style.BRIGHT, end = "")
    elif gra in result.get(t):
      print(Back.GREEN, end = "")
    elif bug in result.get(t):
      print(Fore.GREEN, end = "")
    elif fir in result.get(t):
      print(Back.RED, end = "")
      print(Fore.BLACK, end = "")
    elif nor in result.get(t):
      print(Back.WHITE, end = "")
      print(Fore.BLACK, end = "")
    elif fig in result.get(t):
      print(Fore.RED, end = "")
      print(Style.DIM, end = "")
    elif ele in result.get(t):
      print(Back.YELLOW, end = "")
      print(Style.BRIGHT, end = "")
    elif roc in result.get(t):
      print(Fore.YELLOW, end = "")
      print(Style.DIM, end = "")
    elif gro in result.get(t):
      print(Fore.YELLOW, end = "")
    elif ice in result.get(t):
      print(Back.CYAN, end = "")
      print(Style.BRIGHT, end = "")
    elif poi in result.get(t):
      print(Fore.MAGENTA, end = "")
      print(Style.BRIGHT, end = "")
    elif dar in result.get(t):
      print(Back.BLACK, end = "")
    elif ste in result.get(t):
      print(Fore.WHITE, end = "")
      print(Style.DIM, end = "")
      
    elif gho in result.get(t):
      print(Back.MAGENTA, end = "")
      
    elif dra in result.get(t):
      print(Fore.MAGENTA, end = "")
      print(Style.DIM, end = "")

    for key,value in result.items():
      print(key,value)
pick = Pokemon(none,none,none,none,none,none)
result = {n: "", numb :0, t: "", pre: "", post:"",des:""}

def Start():
     
  choice = input("Enter a number 0-155 or Type Random: ")
  print('')
  if choice in useablenums: #either picks the number the user entered or randomizes the outcome
    choice = choice
  elif choice.lower() == "random":
    choice = random.choice(randomnums)
  else:
    choice = truerandom
    print("Please FOLLOW DIRECTIONS")
  window = pygame.display.set_mode((900,450))
  
#represents the different outcomes of result due to setting parameters for the Pokemon class

  if choice == '0':
    pick = Pokemon("Victini", choice, psy+"/"+fir,none,none,victini)
    window.fill(firC)
    window.blit(Victini,(50,10))
  elif choice == '1':
    pick = Pokemon("Snivy", choice, gra, none, "Servine",snivy)
    window.fill(graC)
    window.blit(SnivyFix,(50,10))
  elif choice == '2':
    pick = Pokemon("Servine", choice, gra, "Snivy", "Serperior",servine)
    window.fill(graC)
    window.blit(Servine,(50,10))
  elif choice == '3':
    pick = Pokemon("Serperior", choice, gra, "Servine", none,serperior)
    window.fill(graC)
    window.blit(Serperior,(50,10))
  elif choice == '4':
    pick = Pokemon("Tepig", choice, fir, none, "Pignite",tepig)
    window.fill(firC)
    window.blit(Tepig,(50,10))
  elif choice == '5':
    pick = Pokemon("Pignite", choice, fir+"/"+fig, "Tepig", "Emboar",pignite)
    window.fill(figC)
    window.blit(Pignite,(50,10))
  elif choice == '6':
    pick = Pokemon("Emboar", choice, fir+"/"+fig, "Pignite",none,emboar)
    window.fill(figC)
    window.blit(Emboar,(50,10))
  elif choice == '7':
    pick = Pokemon("Oshawott",choice, wat, none, "Dewott",oshawott)
    window.fill(watC)
    window.blit(Oshawott,(50,10))
  elif choice == '8':
    pick = Pokemon("Dewott", choice, wat, "Oshawott", "Samurott",dewott)
    window.fill(watC)
    window.blit(Dewott,(50,10))
  elif choice == '9':
    pick = Pokemon("Samurott", choice, wat, "Dewott",none,samurott)
    window.fill(watC)
    window.blit(Samurott,(50,10))
  elif choice == '10':
    pick = Pokemon("Patrat", choice, nor, none, "Watchdog",patrat)
    window.fill(norC)
    window.blit(PatratFix,(50,10))
    window.blit(Patrat2Fix,(250,10))
  elif choice == '11':
    pick = Pokemon("Watchog", choice, nor, "Patrat",none,watchog)
    window.fill(norC)
    window.blit(Watchog,(50,10))
  elif choice == '12':
    pick = Pokemon("Lillipup", choice, nor, none, "Herdier",lillipup)
    window.fill(norC)
    window.blit(Lillipup,(50,10))
  elif choice == '13':
    pick = Pokemon("Herdier", choice, nor, "Lillipup", "Stoutland",herdier)
    window.fill(norC)
    window.blit(Herdier,(50,10))
  elif choice == '14':
    pick = Pokemon("Stoutland", choice, nor, "Herdier", none,stoutland)
    window.fill(norC)
    window.blit(Stoutland,(50,10))
  elif choice == '15':
    pick = Pokemon("Purrloin", choice, dar, none, "Liepard",purrloin)
    window.fill(darC)
    window.blit(Purrloin,(50,10))
  elif choice == '16':
    pick = Pokemon("Liepard", choice, dar, "Purrlion", none, liepard)
    window.fill(darC)
    window.blit(Liepard,(50,10))
  elif choice == '17':
    pick = Pokemon("Pansage", choice, gra, none, "Simisage",pansage)
    window.fill(graC)
    window.blit(Pansage,(50,10))
  elif choice == '18':
    pick = Pokemon("Simisage", choice, gra, "Pansage", none,simisage)
    window.fill(graC)
    window.blit(Simisage,(50,10))
  elif choice == '19':
    pick = Pokemon("Pansear", choice, fir, none, "Simisear",pansear)
    window.fill(firC)
    window.blit(Pansear,(50,10))
  elif choice == '20':
    pick = Pokemon("Simisear", choice, fir, "Pansear", none,simisear)
    window.fill(firC)
    window.blit(Simisear,(50,10))
  elif choice == '21':
    pick = Pokemon("Panpour", choice, wat, none, "Simipour",panpour)
    window.fill(watC)
    window.blit(PanpourFix,(50,10))
  elif choice == '22':
    pick = Pokemon("Simipour", choice, wat, "Panpour", none,simipour)
    window.fill(watC)
    window.blit(Simipour,(50,10))
  elif choice == '23':
    pick = Pokemon("Munna", choice, psy, none, "Musharna",munna)
    window.fill(psyC)
    window.blit(Munna,(50,10))
  elif choice == '24':
    pick = Pokemon("Musharna", choice, psy, "Munna", none,musharna)
    window.fill(psyC)
    window.blit(Musharna,(50,10))
  elif choice == '25':
    pick = Pokemon("Pidove", choice, nor+"/"+fly, none, "Tranquill",pidove)
    window.fill(norC)
    window.blit(Pidove,(50,10))
  elif choice == '26':
    pick = Pokemon("Tranquill", choice, nor+"/"+fly, "Pidove", "Unfezant",tranquill)
    window.fill(norC)
    window.blit(Tranquill,(50,10))
  elif choice == '27':
    pick = Pokemon("Unfezant", choice, nor+"/"+fly, "Tranquill", none,unfezant)
    window.fill(norC)
    window.blit(Unfezant,(25,10))
    window.blit(Unfezant2,(350,10))
  elif choice == '28':
    pick = Pokemon("Blitzle", choice, ele, none, "Zebstrika",blitzle)
    window.fill(eleC)
    window.blit(Blitzle,(50,10))
  elif choice == '29':
    pick = Pokemon("Zebstrika", choice, ele, "Blitzle", none, zebstrika) 
    window.fill(eleC)
    window.blit(Zebstrika,(50,10))
  elif choice == '30':
    pick = Pokemon("Roggenrola", choice, roc, none, "Boldore",roggenrola)
    window.fill(rocC)
    window.blit(Roggenrola,(50,10))
  elif choice == '31':
    pick = Pokemon("Boldore", choice, roc, "Roggenrola", "Gigalith",boldore)
    window.fill(rocC)
    window.blit(Boldore,(50,10))
  elif choice == '32':
    pick = Pokemon("Gigalith", choice, roc, "Boldore", none,gigalith)
    window.fill(rocC)
    window.blit(Gigalith,(50,10))
  elif choice == '33':
    pick = Pokemon("Woobat", choice, psy+"/"+fly, none, "Swoobat",woobat)
    window.fill(flyC)
    window.blit(Woobat,(50,10))
  elif choice == '34':
    pick = Pokemon("Swoobat", choice, psy+"/"+fly, "Woobat", none,swoobat)
    window.fill(flyC)
    window.blit(Swoobat,(50,10))
  elif choice == '35':
    pick = Pokemon("Drilbur", choice, gro, none, "Excadrill",drilbur)
    window.fill(groC)
    window.blit(Drilbur,(50,10))
  elif choice == '36':
    pick = Pokemon("Excadrill", choice, gro+"/"+ste, "Drilbur", none,excadrill)
    window.fill(steC)
    window.blit(Excadrill,(50,10))
  elif choice == '37':
    pick = Pokemon("Audino", choice, nor, none, none,audino) 
    window.fill(norC)
    window.blit(Audino,(50,10))
  elif choice == '38':
    pick = Pokemon("Timburr", choice, fig, none, "Gurdurr",timburr)
    window.fill(figC)
    window.blit(Timburr,(50,10))
  elif choice == '39':
    pick = Pokemon("Gurdurr", choice, fig, "Timburr", none,gurdurr)
    window.fill(figC)
    window.blit(Gurdurr,(50,10))
  elif choice == '40':
    pick = Pokemon("Conkeldurr", choice, fig, "Gurdurr", none,conkeldurr)
    window.fill(figC)
    window.blit(Conkeldurr,(50,10))
  elif choice == '41':
    pick = Pokemon("Tympole", choice, wat, none, "Palpitoad",tympole)
    window.fill(watC)
    window.blit(Tympole,(50,10))
  elif choice == '42':
    pick = Pokemon("Palpitoad", choice, wat+"/"+gro, "Tympole", "Seismitoad",palpitoad)
    window.fill(groC)
    window.blit(Palpitoad,(50,10))
  elif choice == '43':
    pick = Pokemon("Seismitoad", choice, wat+"/"+gro, "Palpitoad", none,seismitoad)
    window.fill(groC)
    window.blit(Seismitoad,(50,10))
  elif choice == '44':
    pick = Pokemon("Throh", choice, fig, none, none,throh)
    window.fill(figC)
    window.blit(Throh,(50,10))
  elif choice == '45':
    pick = Pokemon("Sawk", choice, fig, none, none,sawk)
    window.fill(figC)
    window.blit(Sawk,(50,10))
  elif choice == '46':
    pick = Pokemon("Sewaddle", choice, bug+"/"+gra, none, "Swadloon",sewaddle)
    window.fill(graC)
    window.blit(Sewaddle,(50,10))
  elif choice == '47':
    pick = Pokemon("Swadloon", choice, bug+"/"+gra, "Sewaddle", none,swadloon)
    window.fill(graC)
    window.blit(Swadloon,(50,10))
  elif choice == '48':
    pick = Pokemon("Leavanny", choice, bug+"/"+gra, "Swadloon", none,leavanny)
    window.fill(graC)
    window.blit(Leavanny,(50,10))
  elif choice == '49':
    pick = Pokemon("Venipede", choice, bug+"/"+poi, none, "Whirlipede",venipede)
    window.blit(Venipede,(50,10))
    window.fill(poiC)
  elif choice == '50':
    pick = Pokemon("Whirlipede", choice, bug+"/"+poi, "Venipede", none,whirlipede)
    window.fill(poiC)
    window.blit(Whirlipede,(50,10))
  elif choice == '51':
    pick = Pokemon("Scolipede", choice, bug+"/"+poi, "Whirlipede", none,scolipede) 
    window.fill(poiC)
    window.blit(Scolipede,(50,10))
  elif choice == '52':
    pick = Pokemon("Cottonee", choice, gra, none, "Whimsicott",cottonee)
    window.fill(graC)
    window.blit(Cottonee,(50,10))
  elif choice == '53':
    pick = Pokemon("Whimsicott", choice, gra, "Cottonee", none, whimsicott)
    window.fill(graC)
    window.blit(Whimsicott,(50,10))
  elif choice == '54':
    pick = Pokemon("Petilil", choice, gra, none, "Lilligant",petilil)
    window.fill(graC)
    window.blit(Petilil,(50,10))
  elif choice == '55':
    pick = Pokemon("Lilligant", choice, gra, "Petilil", none, lilligant)
    window.fill(graC)
    window.blit(Lilligant,(50,10))
  elif choice == '56':
    pick = Pokemon("Basculin", choice, wat, none, none,basculin)
    window.fill(watC)
    window.blit(Basculin,(50,10))
  elif choice == '57':
    pick = Pokemon("Sandile", choice, gro+"/"+dar, none, "Krokorok",sandile)
    window.fill(darC)
    window.blit(Sandile,(50,10))
  elif choice == '58':
    pick = Pokemon("Krokorok", choice, gro+"/"+dar, "Sandile", "Krookodile",krokorok)
    window.fill(darC)
    window.blit(Krokorok,(50,10))

  elif choice == '59':
    pick = Pokemon("Krookodile", choice, gro+"/"+dar, "Krokorok", none, krookodile)
    window.fill(darC)
    window.blit(Krookodile,(50,10))
  elif choice == '60':
    pick = Pokemon("Darumaka", choice, fir, none, "Darmanitan",darumaka)
    window.fill(firC)
    window.blit(Darumaka,(50,10))
  elif choice == '61':
    pick = Pokemon("Darmanitan", choice, fir+"| "+fir+"/"+psy, "Darumaka", none, darmanitan)
    window.fill(firC)
    window.blit(Darmanitan,(50,10))
    window.blit(Darmanitan2,(150,200))
  elif choice == '62':
    pick = Pokemon("Maractus", choice, gra, none, none,maractus)
    window.fill(graC)
    window.blit(Maractus,(50,10))
  elif choice == '63':
    pick = Pokemon("Dwebble", choice, bug+"/"+roc, none, "Crustle",dwebble)
    window.fill(rocC)
    window.blit(Dwebble,(25,10))
    window.blit(Dwebble2,(350,10))
  elif choice == '64':
    pick = Pokemon("Crustle", choice, bug+"/"+roc, "Dwebble", none, crustle)
    window.fill(rocC)
    window.blit(Crustle,(50,10))
  elif choice == '65':
    pick = Pokemon("Scraggy", choice, dar+"/"+fig, none, "Scrafty",scraggy)
    window.fill(figC)
    window.blit(Scraggy,(50,10))
  elif choice == '66':
    pick = Pokemon("Scrafty", choice, dar+"/"+fig, "Scraggy", none,scrafty)
    window.fill(figC)
    window.blit(Scrafty,(50,10))
  elif choice == '67':
    pick = Pokemon("Sigilyph", choice, psy+"/"+fly, none, none,sigilyph)
    window.fill(flyC)
    window.blit(SigilyphFix,(50,10))
  elif choice == '68':
    pick = Pokemon("Yamask", choice, gho, none, "Cofagrigus",yamask)
    window.fill(ghoC)
    window.blit(Yamask,(50,10))
  elif choice == '69':
    pick = Pokemon("Cofagrigus", choice, gho, "Yamask", none, cofagrigus)
    window.fill(ghoC)
    window.blit(Cofagrigus,(25,10))
    window.blit(Cofagrigus2,(350,10))
  elif choice == '70':
    pick = Pokemon("Tirtouga", choice, wat+"/"+roc, none,"Carracosta",tirtouga)
    window.fill(rocC)
    window.blit(Tirtouga,(50,10))
  elif choice == '71':
    pick = Pokemon("Carracosta", choice, wat+"/"+roc, "Tirtouga", none, carracosta)
    window.fill(rocC)
    window.blit(Carracosta,(50,10))
  elif choice == '72':
    pick = Pokemon("Archen", choice, roc+"/"+fly, none, "Archeops",archen)
    window.fill(flyC)
    window.blit(Archen,(50,10))
  elif choice == '73':
    pick = Pokemon("Archeops", choice, roc+"/"+fly, "Archen", none, archeops)
    window.fill(flyC)
    window.blit(Archeops,(50,10))
  elif choice == '74':
    pick = Pokemon("Trubbish", choice, poi, none, "Garbodor",trubbish)
    window.fill(poiC)
    window.blit(Trubbish,(50,10))
  elif choice == '75':
    pick = Pokemon("Garbodor", choice, poi, "Trubbish", none, garbodor)
    window.fill(poiC)
    window.blit(Garbodor,(50,10))
  elif choice == '76':
    pick = Pokemon("Zorua", choice, dar, none,"Zoroark",zorua)
    window.fill(darC)
    window.blit(Zorua,(50,10))
    window.blit(Zorua2,(350,10))
    window.blit(Zorua3,(300,200))
  elif choice == '77':
    pick = Pokemon("Zoroark", choice, dar, "Zorua", none, zoroark)
    window.fill(darC)
    window.blit(Zoroark,(50,10))
  elif choice == '78':
    pick = Pokemon("Minccino", choice, nor, none, "Cinccino",minccino)
    window.fill(norC)
    window.blit(Minccino,(50,10))
  elif choice == '79':
    pick = Pokemon("Cinccino", choice, nor, "Minccino", none, cinccino)
    window.fill(norC)
    window.blit(Cinccino,(50,10))
  elif choice == '80':
    pick = Pokemon("Gothita", choice, psy, none,"Gothorita",gothita)
    window.fill(psyC)
    window.blit(Gothita,(50,10))
  elif choice == '81':
    pick = Pokemon("Gothorita", choice, psy, "Gothita","Gothitelle",gothorita)
    window.fill(psyC)
    window.blit(Gothorita,(50,10))
  elif choice == '82':
    pick = Pokemon("Gothitelle", choice, psy, "Gothorita", none, gothitelle)
    window.fill(psyC)
    window.blit(Gothitelle,(50,10))
  elif choice == '83':
    pick = Pokemon("Solosis", choice, psy, none, "Duosion",solosis)
    window.fill(psyC)
    window.blit(Solosis,(50,10))
  elif choice == '84':
    pick = Pokemon("Duosion", choice, psy, "Solosis", none, duosion)
    window.fill(psyC)
    window.blit(Duosion,(50,10))
  elif choice == '85':
    pick = Pokemon("Reuniclus", choice, psy, "Duosion", none, reuniclus)
    window.fill(psyC)
    window.blit(Reuniclus,(50,10))
  elif choice == '86':
    pick = Pokemon("Ducklett", choice, wat+"/"+fly, none, "Swanna",ducklett)
    window.fill(flyC)
    window.blit(Ducklett,(50,10))
  elif choice == '87':
    pick = Pokemon("Swanna", choice, wat+"/"+fly, "Ducklett", none,swanna)
    window.fill(flyC)
    window.blit(Swanna,(50,10))
  elif choice == '88':
    pick = Pokemon("Vanillite", choice, ice, none, "Vanillish",vanillite)
    window.fill(iceC)
    window.blit(Vanillite,(50,10))
  elif choice == '89':
    pick = Pokemon("Vanillish", choice, ice, "Gothorita", none,vanillish)
    window.fill(iceC)
    window.blit(Vanillish,(50,10))
  elif choice == '90':
    pick = Pokemon("Vanilluxe", choice, ice, "Vanillish", none,vanilluxe)
    window.fill(iceC)
    window.blit(Vanilluxe,(50,10))
  elif choice == '91':
    pick = Pokemon("Deerling", choice, nor+"/"+gra, "Gothorita", none,deerling)
    window.fill(graC)
    window.blit(Deerling,(25,10))
    window.blit(Deerling2,(250,160))
  elif choice == '92':
    pick = Pokemon("Sawsbuck", choice, nor+"/"+gra, "Deerling", none,sawsbuck)
    window.fill(graC)
    window.blit(Sawsbuck,(25,10))
    window.blit(Sawsbuck2Fix,(360,10))
  elif choice == '93':
    pick = Pokemon("Emolga", choice, ele+"/"+fly, none, none,emolga)
    window.fill(flyC)
    window.blit(Emolga,(50,10))
  elif choice == '94':
    pick = Pokemon("Karrablast", choice, bug, none, none,karrablast)
    window.fill(bugC)
    window.blit(Karrablast,(50,10))
  elif choice == '95':
    pick = Pokemon("Escavalier", choice, bug+"/"+ste, "Karrablast", none,escavalier)
    window.fill(steC)
    window.blit(Escavalier,(50,10))
  elif choice == '96':
    pick = Pokemon("Foongus", choice, gra+"/"+poi, none,"Amoonguss",foongus)
    window.fill(poiC)
    window.blit(Foongus,(50,10))
  elif choice == '97':
    pick = Pokemon("Amoonguss", choice, gra+"/"+poi, "Foongus", none,amoonguss)
    window.fill(poiC)
    window.blit(Amoonguss,(25,10))
    window.blit(Amoonguss2,(350,10))
  elif choice == '98':
    pick = Pokemon("Frillish", choice, wat+"/"+gho, none, "Jellicent",frillish)
    window.fill(ghoC)
    window.blit(Frillish,(50,10))
  elif choice == '99':
    pick = Pokemon("Jellicent", choice, wat+"/"+gho, "Frillish", none, jellicent)
    window.fill(ghoC)
    window.blit(Jellicent,(50,10))
  elif choice == '100':
    pick = Pokemon("Alomomola", choice, wat, none, none,alomomola)
    window.fill(watC)
    window.blit(Alomomola,(50,10))
  elif choice == '101':
    pick = Pokemon("Joltik", choice, bug+"/"+ele, none,"Galvantula",joltik)
    window.fill(eleC)
    window.blit(Joltik,(50,10))
  elif choice == '102':
    pick = Pokemon("Galvantula", choice, bug+"/"+ele, "Joltik", none, galvantula)
    window.fill(eleC)
    window.blit(Galvantula,(50,10))
  elif choice == '103':
    pick = Pokemon("Ferroseed", choice, gra+"/"+ste, none, "Ferrothorn",ferroseed)
    window.fill(steC)
    window.blit(Ferroseed,(50,10))
  elif choice == '104':
    pick = Pokemon("Ferrothorn", choice, gra+"/"+ste, "Ferroseed", none, ferrothorn)
    window.fill(steC)
    window.blit(Ferrothorn,(50,10))
  elif choice == '105':
    pick = Pokemon("Klink", choice, ste, none, "Klang",klink)
    window.fill(steC)
    window.blit(Klink,(50,10))
  elif choice == '106':
    pick = Pokemon("Klang", choice, ste, "Klink", "Klinklang",klang)
    window.fill(steC)
    window.blit(Klang,(50,10))
  elif choice == '107':
    pick = Pokemon("Klinklang", choice, ste, "Klang", none,klinklang)
    window.fill(steC)
    window.blit(Klinklang,(50,10))
  elif choice == '108':
    pick = Pokemon("Tynamo", choice, ele, none, "Eelektrik",tynamo)
    window.fill(eleC)
    window.blit(Tynamo,(50,10))
  elif choice == '109':
    pick = Pokemon("Eelektrik", choice, ele, "Tynamo", "Eelektross",eelektrik)
    window.fill(eleC)
    window.blit(Eelektrik,(50,10))
  elif choice == '110':
    pick = Pokemon("Eelektross", choice, ele, "Eelektrik", none,eelektross)
    window.fill(eleC)
    window.blit(Eelektross,(50,10))
  elif choice == '111':
    pick = Pokemon("Elgyem", choice, psy, none, "Beheeyem",elgyem)
    window.fill(psyC)
    window.blit(Elgyem,(50,10))
  elif choice == '112':
    pick = Pokemon("Beheeyem", choice, psy, "Elgyem", none,beheeyem)
    window.fill(psyC)
    window.blit(Beheeyem,(50,10))
  elif choice == '113':
    pick = Pokemon("Litwick", choice, gho+"/"+fir, none, "Lampent",litwick)
    window.fill(firC)
    window.blit(Litwick,(50,10))
  elif choice == '114':
    pick = Pokemon("Lampent", choice, gho+"/"+fir, "Litwick", "Chandelure",lampent)
    window.fill(firC)
    window.blit(Lampent,(50,10))
  elif choice == '115':
    pick = Pokemon("Chandelure", choice, gho+"/"+fir, "Lampent", none,chandelure)
    window.fill(firC)
    window.blit(Chandelure,(50,10))
  elif choice == '116':
    pick = Pokemon("Axew", choice, dra, none, "Fraxure",axew)
    window.fill(draC)
    window.blit(Axew,(50,10))
  elif choice == '117':
    pick = Pokemon("Fraxure", choice, dra, "Axew", "Haxorus",fraxure)
    window.fill(draC)
    window.blit(Fraxure,(50,10))
  elif choice == '118':
    pick = Pokemon("Haxorus", choice, dra, "Fraxure", none,haxorus)
    window.fill(draC)
    window.blit(Haxorus,(25,10))
    window.blit(Haxorus2Fix,(350,10))
  elif choice == '119':
    pick = Pokemon("Cubchoo", choice, ice, none, "Beartic",cubchoo)
    window.fill(iceC)
    window.blit(Cubchoo,(50,10))
  elif choice == '120':
    pick = Pokemon("Beartic", choice, ice, "Cubchoo", none,beartic)
    window.fill(iceC)
    window.blit(Beartic,(50,10))
  elif choice == '121':
    pick = Pokemon("Cryogonal", choice, ice, none, none,cryogonal)
    window.fill(iceC)
    window.blit(Cryogonal,(50,10))
  elif choice == '122':
    pick = Pokemon("Shelmet", choice, bug, none,"Accelgor",shelmet)
    window.fill(bugC)
    window.blit(Shelmet,(50,10))
  elif choice == '123':
    pick = Pokemon("Accelgor", choice, bug, "Shelmet", none,accelgor)
    window.fill(bugC)
    window.blit(Accelgor,(50,10))
  elif choice == '124':
    pick = Pokemon("Stunfisk", choice, gro+"/"+ele, none, none,stunfisk)
    window.fill(eleC)
    window.blit(Stunfisk,(50,10))
  elif choice == '125':
    pick = Pokemon("Mienfoo", choice, fig,none, "Mienshao",mienfoo)
    window.fill(figC)
    window.blit(Mienfoo,(50,10))
  elif choice == '126':
    pick = Pokemon("Mienshao", choice, fig, "Mienfoo", none,mienshao)
    window.fill(figC)
    window.blit(Mienshao,(50,10))
  elif choice == '127':
    pick = Pokemon("Druddigon", choice, dra, none, none,druddigon)
    window.fill(draC)
    window.blit(Druddigon,(50,10))
  elif choice == '128':
    pick = Pokemon("Golett", choice, gro+"/"+gho, none, "Golurk",golett)
    window.fill(ghoC)
    window.blit(Golett,(50,10))
  elif choice == '129':
    pick = Pokemon("Golurk", choice, gro+"/"+gho, "Golett", none,golurk)
    window.fill(ghoC)
    window.blit(Golurk,(50,10))
  elif choice == '130':
    pick = Pokemon("Pawniard", choice, dar+"/"+ste, none, "Bisharp",pawniard)
    window.fill(steC)
    window.blit(Pawniard,(50,10))
  elif choice == '131':
    pick = Pokemon("Bisharp", choice, dar+"/"+ste, "Pawniard", none,bisharp)
    window.fill(steC)
    window.blit(Bisharp,(50,10))
  elif choice == '132':
    pick = Pokemon("Bouffalant", choice, nor, none, none,bouffalant)
    window.fill(norC)
    window.blit(Bouffalant,(50,10))
  elif choice == '133':
    pick = Pokemon("Rufflet", choice, nor+"/"+fly,none, "Braviary",rufflet)
    window.fill(flyC)
    window.blit(Rufflet,(50,10))
  elif choice == '134':
    pick = Pokemon("Braviary", choice, nor+"/"+fly, "Rufflet", none,braviary)
    window.fill(flyC)
    window.blit(Braviary,(50,10))
  elif choice == '135':
    pick = Pokemon("Vullaby", choice, dar+"/"+fly, none,"Mandibuzz",vullaby)
    window.fill(flyC)
    window.blit(Vullaby,(50,10))
  elif choice == '136':
    pick = Pokemon("Mandibuzz", choice, dar+"/"+fly, "Vullaby", none,mandibuzz)
    window.fill(flyC)
    window.blit(Mandibuzz,(50,10))
  elif choice == '137':
    pick = Pokemon("Heatmor", choice, fir, none, none,heatmor)
    window.fill(firC)
    window.blit(Heatmor,(50,10))
  elif choice == '138':
    pick = Pokemon("Durant", choice, bug+"/"+ste, none, none,durant)
    window.fill(steC)
    window.blit(Durant,(50,10))
  elif choice == '139':
    pick = Pokemon("Deino", choice, dar+"/"+dra, none, "Zweilous",deino)
    window.fill(draC)
    window.blit(Deino,(50,10))
  elif choice == '140':
    pick = Pokemon("Zweilous", choice, dar+"/"+dra, "Deino", "Hydreigon",zweilous)
    window.fill(draC)
    window.blit(Zweilous,(50,10))
  elif choice == '141':
    pick = Pokemon("Hydreigon", choice, dar+"/"+dra, "Zweilous", none, hydreigon)
    window.fill(draC)
    window.blit(Hydreigon,(50,10))
    window.blit(Hydreigon2,(370,10))
  elif choice == '142':
    pick = Pokemon("Larvesta", choice, bug+"/"+fir, none, "Volcarona",larvesta)
    window.fill(firC)
    window.blit(Larvesta,(50,10))
  elif choice == '143':
    pick = Pokemon("Volcarona", choice, bug+"/"+fir, "Larvesta", none, volcarona)
    window.fill(firC)
    window.blit(Volcarona,(50,10))
  elif choice == '144':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Cobalion", choice, ste+"/"+fig, none, none,cobalion)
    window.fill(figC)
    window.blit(Cobalion,(50,10))
  elif choice == '145':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Terrakion", choice, roc+"/"+fig, none, none,terrakion)
    window.fill(figC)
    window.blit(Terrakion,(50,10))
  elif choice == '146':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Virizion", choice, gra+"/"+fig, none, none,virizion)
    window.fill(figC)
    window.blit(Virizion,(50,10))
  elif choice == '147':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Tornadus", choice, fly, none, none,tornadus)
    window.fill(flyC)
    window.blit(Tornadus,(20,10))
    window.blit(Tornadus2,(350,10))
  elif choice == '148':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Thundurus", choice, ele+"/"+fly, none, none,thundurus)
    window.fill(flyC)
    window.blit(Thundurus,(50,10))
  elif choice == '149':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Reshiram", choice, dra+"/"+fir, none, none,reshiram)
    window.fill(draC)
    window.blit(Reshiram,(50,10))
  elif choice == '150':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Zekrom", choice, dra+"/"+ele, none, none,zekrom)
    window.fill(draC)
    window.blit(Zekrom,(20,10))
    window.blit(Zekrom2,(325,10))
  elif choice == '151':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Landorus", choice, gro+"/"+fly, none, none,landorus)
    window.fill(flyC)
    window.blit(Landorus,(50,10))
  elif choice == '152':
    print(Back.YELLOW, end = "")
    print("Legendary", end = "")
    print(Back.RESET)
    pick = Pokemon("Kyurem", choice, dra+"/"+ice, none, none,kyurem)
    window.fill(draC)
    window.blit(KyuremFix,(10,10))
    window.blit(Kyurem2,(260,10))
    window.blit(Kyurem3,(100,150))
  elif choice == '153':
    print(Back.YELLOW, end = "")
    print("Mythical", end = "")
    print(Back.RESET)
    pick = Pokemon("Keldeo", choice, wat+"/"+fig, none, none,keldeo)
    window.fill(figC)
    window.blit(Keldeo,(20,10))
    window.blit(Keldeo2,(330,10))
  elif choice == '154':
    print(Back.YELLOW, end = "")
    print("Mythical", end = "")
    print(Back.RESET)
    pick = Pokemon("Meloetta", choice, nor+"/"+psy+"|"+nor+"/"+fig, none, none,meloetta)
    window.fill(norC)
    window.blit(Meloetta,(50,10))
  elif choice == '155':
    pick = Pokemon("Genesect", choice, bug+"/"+ste, none, none,genesect)
    window.fill(steC)
    window.blit(Genesect,(50,10))
  
  pick.info()#Runs result information then resets style/color changes before running again
  pygame.display.update()
  print(Back.RESET, end = "")
  print(Fore.RESET, end = "")
  print(Style.RESET_ALL)
  
  Start()