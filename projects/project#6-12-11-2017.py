import random
import math

turn=0
p1= 0
newp1=0
bankp1=0
p2 = 0
p1action = "roll"

while (p1<= 100 or p2<= 100):
  turn+=1
  while (p1action !="hold" and p1!= 1):
    p1 = newp1
    p1 = random.randint(1,6)
    if (p1==1):
      bankp1 = bankp1 + 0
      newp1 = 0
      print("Turn:" + str(turn) +'\nPlayer 1 rolled a ' + str(p1) +". You accumulated 0 points this turn. Your bank total is now " + str(bankp1))
    else:
      newp1= newp1 +p1
      print("Turn:" + str(turn) +'\nPlayer 1 rolled a ' + str(p1) +". Your temporary total for this turn is " + str(newp1))
      p1action = input('Would you like to "roll" or "hold" ?')
    if (p1action== "hold"):
      bankp1 = bankp1 + newp1
      newp1=0
      print("You accumulated a score of " + str(bankp1) + " in turn " + str(turn))

#make sure to reset newp1 and p1 after you bank it
#after p1 is done with rolling, either by "hold" or rolling a 1, switch it over to p2 by making p2 action = "roll"
