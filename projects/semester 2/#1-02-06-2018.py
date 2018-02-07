def perfect_number(n):
  divisors =[]
  sum=0
  for i in range(1,n):
    if n%i ==0:
      divisors.append(i)
  for i in divisors:
    sum = sum+i
  if sum == n:
    return True
  else:
    return False
