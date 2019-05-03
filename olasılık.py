#24 defa atılan zarda double 6 gelme olasılığı.
import random
def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])
def checkPascal(numTrials):
    numWins = 0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print(numWins/numTrials)

#checkPascal(100000) # 100000 defa çağırınca gerçek sonucu görüyoruz %50 ihtimal

def playHand1(numTrials):
    for i in range(numTrials):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            pass
        elif throw == 2 or throw == 3 or throw == 12:
            pass
        else:
            point = rollDie() + rollDie()
            while throw == point:
                if point == 7:

                    break
                point = rollDie()



class CrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = 0, 0
        self.dpWins, self.dpLosses, self.dpPushes = 0, 0, 0  #dpPushes 12 gelince tekrar oynatıyor.

    def playHand(self):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else:
                self.dpWins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie()
                if throw == point:
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    self.dpWins += 1
                    break

def tryCrapsGame(numTrials):
    c = CrapsGame()
    for i in range(numTrials):
        c.playHand()
    print(c.passWins / numTrials)

tryCrapsGame(100000)
