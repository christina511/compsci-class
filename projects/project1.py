import math
lenAB= int(input("Enter a length for AB: "))
lenBC= int(input("Ener a length for BC: "))

lenAC= math.hypot(lenAB,lenBC)
midpt= lenAC/2
angle= math.degrees(math.asin(midpt/lenBC))
if (angle-angle//1) >= 0.5:
    angle = int(angle + 1)
else: 
   angle = int(angle)
print("This is the angle of triangle MBC to the nearest degree: " + str(angle))
