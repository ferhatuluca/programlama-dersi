import random
def get_n_random_integer(n):
    numbers = []
    for i in range(n):
        s = random.randint(-10,10)
        numbers.append(s)
    return numbers
    
def get_mean_for_n_integer(numbers):#ortalama
    toplam = 0
    kactane = 0
    for sayi in numbers:
        toplam = toplam + sayi
        kactane = kactane + 1
    return toplam / kactane
    
    
def get_std_for_n_integer(numbers):#standart sapma
    toplam = 0
    kactane = 0
    ortalama = get_mean_for_n_integer(numbers)
    
    for sayi in numbers:
        toplam = toplam + (sayi - ortalama) ** 2
        kactane = kactane + 1
        
    varyans_1 = toplam / (kactane - 1)
    std_1 = varyans_1 ** 0.5 #kok alma
    return std_1    

def insertion_sort(numbers):
    sayilar = numbers
    swap = 0
    comparison = 0  
    for i in range(1, len(sayilar)):
        for j in range(i, 0, -1):
            if(sayilar[j] < sayilar[j - 1]):
                swap += 1
                temp = sayilar[j - 1]
                sayilar[j - 1] = sayilar[j]
                sayilar[j] = temp
            else:
                break
            comparison += 1
    return sayilar, swap, comparison
    
def bubble_sort(numbers):
    n = len(numbers)
    swaps = 0
    comparison = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparison +=1
            if numbers[j] > numbers[j+1]:
                swaps += 1
                numbers[j],numbers[j+1] = numbers[j+1], numbers[j]
    
    return swaps, comparison, 

def get_mean_of_swap_in_insertion(numTrials, numInt):
    swaps = []
    for i in range(numTrials):
        sayilar_1 = get_n_random_integer(numInt)
        sayilar_2 = insertion_sort(sayilar_1)
        s_1 = sayilar_2[1]  #swap sayısı
        swaps.append(s_1)
    mean_1 = get_mean_for_n_integer(swaps)
    std_1 = get_std_for_n_integer(swaps)
    return mean_1, std_1
    
def get_mean_of_swap_in_bubble(numTrials, numInt):
    swaps = []
    for i in range(numTrials):
        sayilar_1 = get_n_random_integer(numInt)
        s_1 = bubble_sort(sayilar_1)
        swaps.append(s_1)
        
    mean_1 = get_mean_for_n_integer(swaps)
    std_1 = get_std_for_n_integer(swaps)
    return mean_1, std_1
    
    
numbers = get_n_random_integer(10)
numbers_2 = numbers.copy()
print(numbers)
print(insertion_sort(numbers))
print(get_mean_of_swap_in_insertion(10, 1000))
print(numbers_2)
print(bubble_sort(numbers_2))
print(get_mean_of_swap_in_bubble(10, 1000))
