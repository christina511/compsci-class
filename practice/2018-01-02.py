import math
def RealRoots(a,b,c):
  if ((b**2)-(4*a*c)) <0:
    print("The quadratic is not factorable. The roots are not real.")
  elif ((b**2)-(4*a*c)) >0:
    x= ((-b) + math.sqrt((b**2) - (4*a*c)))/ (2*a)
    y= ((-b) - math.sqrt((b**2) - (4*a*c)))/ (2*a)
    z= math.sqrt(((b**2)-(4*a*c))) - (math.sqrt(((b**2)-(4*a*c)))//1)
    print("The real roots are", x, "and",y)
    if z == 0:
      print("The quadratic is factorable.")
    else:
      print("The quadratic is not factorable.")
  elif ((b**2)-(4*a*c)) == 0:
    x= ((-b) + math.sqrt((b**2) - (4*a*c)))/ (2*a)
    z= math.sqrt(((b**2)-(4*a*c))) - (math.sqrt(((b**2)-(4*a*c)))//1)
    print("There is one real root," , x)
    if z == 0:
      print("The quadratic is factorable.")
    else:
      print("The quadratic is not factorable.")
