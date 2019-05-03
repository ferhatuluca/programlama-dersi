import random
def number_of_list(n):
    #random.seed(100)              #tüm pclerde aynı değer üretir ve değer değişmez.
    liste = []
    for i in range(n):
        liste.append(random.randint(-10, 10))
    return liste

def get_mean_of_list(numbers):
    sum = 0
    how_many = 0
    for number in numbers:
        sum += number
        how_many += 1
    return sum/how_many
#varyans = standart sapma

def get_std_for_n_integar(numbers): 
    sum = 0
    how_many = 0
    mean = get_mean_of_list(numbers)
    for number in numbers:
        sum += (number-mean)**2
        how_many += 1
    var_1 = sum/(how_many-1)
    std_1 = var_1**.5             
    return std_1

def normalizasyon(numbers):
    new_numbers = []
    mean = get_mean_of_list(numbers)
    standart_sapma = get_std_for_n_integar(numbers)
    for number in numbers:
        new_number = (number-mean)/standart_sapma
        new_numbers.append(new_number)
    return new_numbers


def get_mean_one_std_neighbor_ratio(numbers):      
    how_many = 0
    how_many_numbers = 0

    mean = get_mean_of_list(numbers)
    std = get_std_for_n_integar(numbers)

    low = mean-std
    high = mean+std

    for number in numbers:
        how_many_numbers += 1
        if number>low and number<high:
            how_many += 1
    return how_many/how_many_numbers

numbers = number_of_list(5)
mean = get_mean_of_list(numbers)
std = get_std_for_n_integar(numbers)
new_numbers = normalizasyon(numbers)
print(std, numbers, new_numbers)
print(get_mean_of_list(new_numbers))
print(get_std_for_n_integar(new_numbers))     
numbers_1 = number_of_list(10)
print(get_mean_one_std_neighbor_ratio(numbers_1))   
