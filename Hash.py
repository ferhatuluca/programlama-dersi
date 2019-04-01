#Hash tablosunun boyutu asal olmalı.

import random

def create_hash_table(size):
    table = []
    for i in range(size):
        table.append(0)
    return table

def my_Hash(mytablesize, numbertobeinserted):
    return numbertobeinserted%mytablesize

def insertmyhashtable(mytable, numbertobeinserted):
    isCollision = False
    index = my_Hash(len(mytable), numbertobeinserted)
    if mytable[index] == 0:
        mytable[index] = 1
    else:
        isCollision = True
    return isCollision

def mytest(size = 13, numberofinsert = 10):
    m_h_1 = create_hash_table(size)
    c = 0
    for s in range(numberofinsert):
        #number = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        number = random.randint(1, 10000)
        if insertmyhashtable(m_h_1, number) == True:
            c += 1
    return c

print(mytest(703, 50))
