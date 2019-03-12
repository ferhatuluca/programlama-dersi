import math

""" Girilen sayının asal olup/olmadığını bulan,eğer asal değilse çarpanlarını ekrana basan fonksiyon."""

def prime_numbers(x):
    list=[]
    list_asal=[1,x]
    count=False
    for i in range(2,int(x/2)):
        if(x%i == 0):
            list.append(i)
            count = True

    if(count == True):
        return list
    else:
        return "asal"

print(prime_numbers(487))

# ----------------------------------------------->

""" N'e kadar olan asal sayıların ekrana yazdıran fonksiyon. """

def asal(n):
    listA = [2,3]
    count = False
    for i in range(5,n+1):
        for j in listA:
            if(j < i/2):      #Sayımızın yarısına kadar olan elemanlara bölünüyomu diye kontrol ediyoruz.
                if(i % j == 0):
                    count = True
                    break
                    
        if(count == False):
            listA.append(i)
        else:
            count = False

    print(listA)

asal(10000)

# ----------------------------------------------->

""" Bir listedeki ardışık n tane sayının toplamlarını bulan ve bu toplamlar arasından en büyüğü yazdıran fonksiyon."""

def Ardışık_en_büyük(list):
    maximum=0
    ilk = 0
    son = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)+1):
            toplam = sum(list[i:j+1])    # list[i:j] i kapalı aralığından j açık aralağına kadar olan elemanları alıyor. Sum fonksiyonuda bu elemanları topluyor
            if(toplam <= maximum):
              continue
            else:
              maximum = toplam
              ilk = i
              son = j

    print(ilk,"İlk indis",son,"Son indis",maximum,"En büyük eleman")


liste=[-4,-5,8,-3,-2,2]
Ardışık_en_büyük(liste)
