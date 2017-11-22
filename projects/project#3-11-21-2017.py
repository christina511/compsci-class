import math

#program 1: compound interest
p = float(input("How much money have you saved?"))
a = float(input("How much does the item you want to purchase cost?"))
if (p>= a):
  print("You have enough money saved! :D")
if (p< a):
  #A = P(1.07)**t
  print("Sorry but you don't have enough money.")
  a = a/p
  t = (math.log10(a)/math.log10(1.07))
  print("You need to wait " + str(t) + " years before you can buy your item.")

#program 2: reference angle
angle = int(input("Enter a positive angle: "))
while (angle <0):
  angle = int(input("Enter a positive angle: "))
while (angle >360):
  angle = angle%360
if (angle%90 == 0):
  refAngle = "no reference"
if (angle >0 and angle<90):
  refAngle = angle
if (angle>90 and angle<180):
  refAngle = 180 - angle
if (angle > 180 and angle < 270):
  refAngle = angle - 180
if (angle>270 and angle <360):
  refAngle = 360- angle
print("Reference Angle:",refAngle, "degrees")
