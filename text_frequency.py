""" Alınan text dosyasının kelimlerinin frekansının bulunması."""

class myclass():
    def __init__(self):
        f = open("dosya.txt", "r")
        mycontent = f.read()
        mysentences = mycontent.split(".")
        self.mywords = []
        for sentence in mysentences:
            words_in_the_sentence = sentence.split(" ")
            for word_1 in words_in_the_sentence:
                self.mywords.append(word_1)
        """print(self.mywords)
        print("\n", mysentences)
        print("\n", mycontent)"""
        self.myfrequancy_1()
        self.myfrequancy_2()
        self.write_frequancy_1()
        #self.write_frequancy_2()

    def myfrequancy_1(self):
        self.frequency_list_1 = {}
        for word in self.mywords:
            if(word in self.frequency_list_1):
                self.frequency_list_1[word] += 1
            else:
                self.frequency_list_1[word] = 1

    def write_frequancy_1(self):
        for word_1 in self.frequency_list_1:
            print(word_1 + " " + str(self.frequency_list_1[word_1]))
    def myfrequancy_2(self):
        self.frequency_list_2 = {}
        for i in range(len(self.mywords)-1):
            w_1, w_2 = self.mywords[i], self.mywords[i+1]
            if ((w_1, w_2) in self.frequency_list_2):
                self.frequency_list_2[w_1, w_2] += 1
            else:
                self.frequency_list_2[w_1, w_2] = 1

    def write_frequancy_2(self):
        for word_2 in self.frequency_list_2:
            print(word_2 + " " + str())

a = myclass()
