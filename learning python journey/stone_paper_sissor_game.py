import random

def game(random,player):
  if player == random:
    return None
  
  if player =="s":
    if random == "p":
      return False
    elif random == "x":
      return True

  if player =="p":
    if random == "s":
      return True
    elif random == "x":
      return False
    
  if player =="x":
    if random == "s":
      return True
    elif random == "p":
      return False

random=random.randint(1,3)

if random == 1:
  random="s"
elif random == 2:
  random="p"
elif random == 3:
  random="x"

player=str(input("select your choice stone(s) paper (p) sissor(x)"))

print ("you selected " + player)
print("computer selected"+" " + str(random))

a = game(random, player)
if a ==None :
  print("game is a tie")
elif a==True:
  print("you win")
elif a==False:
  print("you lose")