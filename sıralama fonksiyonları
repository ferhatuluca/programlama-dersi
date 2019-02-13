import random
def liste_olustur():
  liste=[]
  for i in range(0,5):
    a=random.randint(0,100)
    liste.append(a)
  return liste

def buble_sort(liste):
  j=0
  count=0
  while(j!=len(liste)-1):
    for i in range(0,len(liste)-1-j):
      if(liste[i]>liste[i+1]):
        a=liste[i]
        liste[i]=liste[i+1]
        liste[i+1]=a
        count=1
    if(count==0):
      break
    j+=1

def selection_sort(liste):
  for i in range(0,len(liste)-1):
    minindex=i
    for j in range(i+1,len(liste)):
      if (liste[j] < liste[minindex]):
        minindex=j
    if (minindex != i):
      deg=liste[minindex]
      liste[minindex]=liste[i]
      liste[i]=deg


liste=liste_olustur()
print(liste)
selection_sort(liste)
print(liste)
