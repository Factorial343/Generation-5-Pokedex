import pygame
from background import Start
'''def Dec():
  choice = int(input("Enter a number 0-146 "))
  global result
  result = {}
  #for i in range(0,158):
  if choice == 0:
    result = {n: "Victini",numb: 0, t: fir+"/"+psy, pre: none,post:none}
  elif choice == 1:
    result = {n: "Snivy",numb: 1, t: gra, pre: none,post:"Servine"}
  elif choice == 2:
    result = {n:"Servine",numb:2, t:gra, pre: "Snivy", post: "Serperior"}
  elif choice == 3:
    result = {n:"Servine",numb:choice, t:gra, pre: "Servine", post: none}
  else:
    pass
    print()
  
  for key,value in result.items():
    print(key,value)
  Dec()
Dec()
'''
pygame.init()
print("Hello, this is a full Pokedéx of the Unova Reigon.\nThe Unova Pokédex was introduced in Generation V through Pokémon Black & White.\nIt is the only Pokédex to contain Pokémon only found in that Generation (with the exception of Generation I).\nYou can explore any of the 156 Pokémon by typing their number into the prompt\n")
Start()
