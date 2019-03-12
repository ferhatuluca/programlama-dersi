""" Kendi çözümüm."""

def bozukpara(n,clist):
    mini = 5000       # Sınır değer : her para biriminden 5000'den fazla kullanılamaz.
    list=[]
    while(n > 0):
        for i in range(len(clist)):
            if(int(n/clist[i]) < mini and n >= clist[i]):
                mini = int(n/clist[i])
                index = i

        list.append([mini,clist[index]])
        n = n - clist[index]*mini
        mini = 5000     # Sınır değeri tekrar güncelliyoruz.
    print(list)

""" Hocanın çözümü"""

def recMC(coinlist,change,knownResults):
    mincoin = change
    if(change in coinlist):
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinlist if c <= change]:
            numcoin = 1 + recMC(coinlist , change - i , knownResults)
            if numcoin < mincoin:
                mincoin=numcoin
                knownResults[change] = mincoin
    return mincoin


coinlist=[1,5,10,25]
bozukpara(40, coinlist)
print(recMC(coinlist,40,[0]*41))
