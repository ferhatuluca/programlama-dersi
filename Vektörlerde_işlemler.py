""" İki vektörün vektörel çarpımı. """

def Vectors_Inner_Product(v,m):
  size=len(v)
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=v[i]*w[i]
  
  t=0
  for i in range(size):
    t=t+my_result[i]
  return t

""" İki vektörün skaler çarpımı. """

def Vectors_scalar_product(alpha,v):
  size=len(v)
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=alpha*v[i]
  return my_result

""" İki vektörün birbirinden çıkarılması. """

def Vektors_Substraction(v,w):
  size=len(v)
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=v[i]-w[i]
  return my_result
  
""" İki vektörün birbirine eklenmesi. """

def Vectors_Addition(v,w):
  size=len(v)
  my_result=[]
  for i in range(size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=v[i]+w[i]
  return my_result

#---------------------------------------
v=[1,2,3,4,5]
w=[8,3,5,7,6]
alpha=8
print(Vectors_Inner_Product(v,w))
print(Vectors_scalar_product(alpha,v))
print(Vektors_Substraction(v,w))
print(Vectors_Addition(v,w))
