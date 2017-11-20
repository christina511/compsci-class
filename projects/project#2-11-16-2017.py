import math
#a = p(1+(r/n))**nt
p = float(input("What is the amount you saved up?"))
r = (int(input("What is your current savings rate in percent?"))/100)
n = int(input("How often does your investment compound per year?"))
a = 2*p
x = (1 + (r/n))
y = a/p 
#y will always be 2
t = ((math.log10(y))/ (n*(math.log10(x))))
print("Your amount will double in " + str(t) + " years")
