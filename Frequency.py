""" Sözlük yapısı ile listedeki elemanların frekansını hesaplama. """

def frequency_dict (liste) :
    freq_dict={}
    for item in liste :
        if (item in freq_dict):
            freq_dict[item] = freq_dict[item]+1
        else:
            freq_dict[item] = 1
    return freq_dict
    

""" Liste yapısı ile listedeki elemanların frekansını hesaplama. """

def frequency_list (liste):
    freq_list = []
    for i in range (len(liste)):
        s = False
        for j in range (len(freq_list)):
            if list[i] == freq_list[j][0] :
                freq_liste[j][1] += 1
                s = True
        if not s:
            freq_list.append([liste[i],1])
    return freq_list
    
    
liste = [2,2,2,3,3,7,54,87,54,69,25,14,7,54,3,7,4,4,12,52]
print(frequency_dict(liste))
print(frequency_list(liste))
