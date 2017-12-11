import random
import math

turn=0
p1= 0
newp1=0
p2 = 0
p1action = "roll"

while (p1<= 100 or p2<= 100):
  turn+=1
  while (p1action !="hold" and p1!= 1):
    p1 = newp1
    p1 = random.randint(1,6)
    newp1= newp1 +p1
    print("Turn:" + str(turn) +'\nPlayer 1 rolled a ' + str(p1) +". Your temporary total is now " + str(newp1))
    p1action = input('Would you like to "roll" or "hold" ?')
  if (p1action== "hold"):
    newp1 = newp1
    print("You accumulated a score of " + str(newp1) + " in turn " + str(turn))
  if (p1==1):
    newp1 =0
