from math import floor
from random import shuffle
    
def merge(A, p, q, r):
    y = q+1-p
    z = r - q
    L = [0] * (y)
    R = [0] * (z)

    for i in range(0 , y): 
        L[i] = A[p + i] 
    for i in range(0 , z): 
        R[i] = A[q + 1 + i]

    i = 0
    j = 0
    k = p

    while i < y and j < z : 
        if L[i] <= R[j]: 
            A[k] = L[i] 
            i += 1
        else: 
            A[k] = R[j] 
            j += 1
        k += 1
  
    while i < y: 
        A[k] = L[i] 
        i += 1
        k += 1
   
    while j < z: 
        A[k] = R[j] 
        j += 1
        k += 1


def mergeSort(A, p, r):
    if p < r :
        q = floor((p + r)/2)
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

A = []
for i in range (1, 150):
    A.append(i)
shuffle(A)
print(A)
mergeSort(A, 0, len(A)-1)
print(A)
