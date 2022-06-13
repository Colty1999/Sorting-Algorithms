import numpy as np


def selection(list):
    for i in range (0, len(lista) ):
        min = lista[i]
        min_nr = i
        for j in range (i, len(lista) ):
            if min > lista[j]:
                min = lista[j]
                min_nr = j
        a = lista[i]
        lista[i] = min
        lista[min_nr] = a
        print(lista)
    

lista = [7,8,5,4,13,9,1,3,2]
selection(lista)