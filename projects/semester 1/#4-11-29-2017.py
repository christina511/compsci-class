month= int(input("Enter a month from 1-12: "))
year = int(input("Enter a year: "))

if (year%4== 0):
  if (year%100 == 0):
    if (year%400 ==0):
      daysYear= 366
    else:
      daysYear = 365
  else:
    daysYear = 366
else: 
  daysYear = 365

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==12):
  daysMonth = 31
if (month == 4 or month == 6 or month == 9 or month ==11):
  daysMonth = 30
if (month ==2 and daysYear == 365):
  daysMonth = 28
if (month ==2 and daysYear == 366):
  daysMonth = 29
  
print("There are " + str(daysMonth) + " days in that month out of " + str(daysYear) + " days in the year " + str(year) +".")
