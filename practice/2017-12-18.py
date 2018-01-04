sum=0
for i in range(1000):
  if i%4==0 or i%7==0:
    sum= sum + i
print("The sum of all the multiples of 4 and 7 below 1000 is " + str(sum) +".")

#checks to if user input is a prime number:
import math
num = int(input("Enter an integer: "))
mid = int(math.sqrt(num))+1
count=0
for x in range(2,mid):
  if num%x==0:
    count+=1
if count>0:
  print(str(num)+" is not a prime number.")
elif count==0:
  print(str(num)+" is a prime number.")
#future steps/challenge: see which is the highest factor
