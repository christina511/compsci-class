import math

addMinutes = int(input("How long is each session (in minutes)?"))

newHours = 8
newMinutes = 0
session = 0

fiveMinutes = input('Want to add 5 minutes in between each session? Enter "yes" or "no": ')

while (fiveMinutes!="yes" and fiveMinutes!= "no"):
  fiveMinutes = input('Bad input! Want to add 5 minutes in between each session? Enter "yes" or "no": ')

if (fiveMinutes == "yes"):
  fiveMinutes = True
if (fiveMinutes == "no"):
  fiveMinutes = False

while (session <8):
  session+=1
  hours = newHours%12
  minutes = newMinutes
  newHours = (newHours + (newMinutes + addMinutes)//60)%12
  newMinutes = (minutes + addMinutes%60)%60
  if(hours%12 == 0):
    hours = 12
  if(newHours%12 ==0):
    newHours = 12
  print("session: " + str(session) +'  '+ str(hours) +":" + '{0:02}'.format(minutes%60) + " - " + str(newHours) + ":" + '{0:02}'.format(newMinutes%60)) 
  if (fiveMinutes == True):
    newMinutes +=5
