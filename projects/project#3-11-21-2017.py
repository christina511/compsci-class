import math
p = float(input("How much money have you saved?"))
a = float(input("How much does the item you want to purchase cost?"))
if (p>= a):
  print("You have enough money saved!")
if (p< a):
  #A = P(1.07)**t
  print("Sorry but you don't have enough money.")
  a = a/p
  t = (math.log10(a)/math.log10(1.07))
  print("You need to wait " + str(t) + " years before you can buy your item.")
