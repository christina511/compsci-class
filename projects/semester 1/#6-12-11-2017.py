import random
import math

print("Let's play Pig!\n")

turn=0
p1= 0
newp1=0
bankp1=0
p2 = 0
newp2 = 0
bankp2=0
p1action = "roll"
p2action = "hold"

while (p1<= 100 or p2<= 100):
  turn+=1
  while (p1action !="hold" and p1!= 1):
    p1 = newp1
    p1 = random.randint(1,6)
    if (p1==1):
      bankp1 = bankp1 + 0
      newp1 = 0
      print("Turn:" + str(turn) +'\nPlayer 1 rolled a ' + str(p1) +". Player 1 accumulated 0 points this turn. Player's 1 bank total is now " + str(bankp1))
      print("**********************************************************")
      p1=0
      p2action = "roll"
      break
    else:
      newp1= newp1 +p1
      print("Turn:" + str(turn) +'\nPlayer 1 rolled a ' + str(p1) +". Player 1's temporary total for this turn is " + str(newp1) + ".")
      p1action = input('Would you like to "roll" or "hold" ?')
    if (p1action== "hold"):
      bankp1 = bankp1 + newp1
      newp1=0
      p1=0
      print("Player 1 accumulated a total bank score of " + str(bankp1) + " by turn " + str(turn))
      if (bankp1 >=100):
        print("Player 1 won!")
        break
      print("**********************************************************")
      p2action = "roll"
      break
  while (p2action !="hold" and p2!= 1):
    p2 = newp2
    p2 = random.randint(1,6)
    if (p2==1):
      bankp2 = bankp2 + 0
      newp2 = 0
      print("Turn:" + str(turn) +'\nPlayer 2 rolled a ' + str(p2) +". Player 2 accumulated 0 points this turn. Player 2's bank total is now " + str(bankp2))
      print("**********************************************************")
      p2=0
      p1action = "roll"
      break
    else:
      newp2= newp2 +p2
      print("Turn:" + str(turn) +'\nPlayer 2 rolled a ' + str(p2) +". Player 2's temporary total for this turn is " + str(newp2))
      p2action = input('Would you like to "roll" or "hold" ?')
    if (p2action== "hold"):
      bankp2 = bankp2 + newp2
      newp2=0
      p2=0
      print("Player 2 accumulated a total bank score of " + str(bankp2) + " by turn " + str(turn))
      if (bankp2 >=100):
        print("Player 2 won!")
        break
      print("**********************************************************")
      p1action = "roll"
      break

#make sure to reset newp1 and p1 after you bank it
#after p1 is done with rolling, either by "hold" or rolling a 1, switch it over to p2 by making p2 action = "roll"
