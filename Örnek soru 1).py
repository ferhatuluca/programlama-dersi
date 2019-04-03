"""NxN tane karakteri NxN matrise atayan bir fonksiyon yazınız.
    a) kendisine aktarılan kelimeyi bu matris üzerinde soldan sağa, sağdan sola, yukarıdan aşağıya, aşağıdan yukarıya
    doğrultularında arayıp olup olmadığını return eden bir fonksiyon."""

import random
def N_by_N_words(n, kelimeler):
    liste = []
    for i in range(n):
        liste.append([])
        for j in range(n):
            liste[i].append(random.choice(kelimeler))
    return liste


def print_list(liste):
    n = len(liste)
    for i in range(n):
        for j in range(n):
            print(liste[i][j], end="  ")
        print("\n")


def find_word_in_list(liste, word):
    lenght_of_list = len(liste)
    lenght_of_word = len(word)
    counter1 = 0
    counter2 = 0
    sayac1 = 0
    sayac2 = 0

    # soldan sağa ve sağdan sola arama yapan kısım.
    for i in range(lenght_of_list):
        for k in range(lenght_of_list-lenght_of_word+1):   #listenin satır uzunluğu ve kelimenin uzuluğunun farkı kadar dönen döngü
            for j in range(lenght_of_word):     # kelime uzunluğu kadar dönen döngü.
                if liste[i][j+k] == word[j]:      # soldan sağa kontrol
                    counter1 += 1
                if liste[i][j+k] == word[lenght_of_word-j-1]:     #sağdan sola kontrol
                    counter2 += 1

            if counter1 == lenght_of_word:
                sayac1 += 1
            if counter2 == lenght_of_word:
                sayac1 += 1

            counter1 = 0
            counter2 = 0

    # yukarıdan aşağı ve aşağıdan yukarı arama yapan kısım.
    for i in range(lenght_of_list):
        for k in range(lenght_of_list-lenght_of_word+1):   #listenin sütün uzunluğu ve kelimenin uzuluğunun farkı kadar dönen döngü
            for j in range(lenght_of_word):     # kelime uzunluğu kadar dönen döngü.
                if liste[j+k][i] == word[j]:      # yukarıdan aşağı kontrol
                    counter1 += 1
                if liste[j+k][i] == word[lenght_of_word-j-1]:     #aşağıdan yukarı kontrol
                    counter2 += 1

            if counter1 == lenght_of_word:
                sayac2 += 1
            if counter2 == lenght_of_word:
                sayac2 += 1

            counter1 = 0
            counter2 = 0

    return sayac1, sayac2

"""
while(True):
    liste = N_by_N_words(10)
    donus =find_word_in_list(liste, "abcd")
    toplam = donus[0] + donus[1]
    if toplam > 3:
        break
"""
word_list = ["a", "b", "c", "d", "e"]
liste = N_by_N_words(5, word_list)
donus = find_word_in_list(liste, "abc")
print_list(liste)
print("{} tane satirlarda, {} tane sütünlarda aradığımız kelime var.".format(donus[0], donus[1]))
