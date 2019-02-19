def fibonacci(n):
  a,b=0,1
  if(n==0):
    return 0
  for i in range(n-1):
    c=a+b
    a=b        # veya a,b=b,a+b
    b=c
  return b

def fibonacci_recursive(n): 
  if(n<2):
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

  #--------------------------------------------------
  

def factoriyel(n):
  s=1
  for i in range(1,n+1):
    s=s*i
  return s

def factoriyel_recursive(n):
  if(n==1):
    return 1
  else:
    return n*factoriyel_recursive(n-1)
    
  #--------------------------------------------------
  #facktoriyelde recursive olsa bile yüksek rakamlarda hesaplıyor

def power(m,n):
  s=1
  for i in range(n):
    s=s*m
  return s

def power_recursive(m,n):
  if(n==0):
    return 1
  elif(n==1):
    return m
  elif(n%2==0):
    return power_recursive(m*m,(n//2))
  elif(n%2!=0):
    return power_recursive(m*m,(n//2))*m

  #---------------------------------------------------
  #kuvvet almada recursive "binary search" mantığında çalıştıgı için daha hızlı.
  #örnek olarak 3^4 için 9^2 ve 81^1 "i hesaplıyor.

print(factoriyel(0))
print(factoriyel_recursive(4))
print(power_recursive(2,10))
