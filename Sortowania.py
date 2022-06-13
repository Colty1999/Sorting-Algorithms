from math import floor
from random import shuffle

#quick

def partition (arr, low, high):
    n = 0
    i = (low - 1)
    for j in range(low, high):
        n +=1
        if arr[j] < arr[high]:
            i=i+1
            argp = arr[i]
            arr[i] = arr[j]
            arr[j] = argp
    argk = arr[i+1]
    arr[i + 1] = arr[high]
    arr[high] = argk
    return (i + 1, n)

def quickSort(arr, low, high):
    n = 0
    if low < high :
        pi, n1 = partition(arr, low, high);
        n2 = quickSort(arr, low, pi - 1);  
        n3 = quickSort(arr, pi + 1, high);
        n = n1 + n2 + n3
    return n

#merge
    
def merge(A, p, q, r):
    m = 0
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
        m += 1
  
    while i < y: 
        A[k] = L[i] 
        i += 1
        k += 1
        m += 1
   
    while j < z: 
        A[k] = R[j] 
        j += 1
        k += 1
        m += 1
    return m


def mergeSort(A, p, r):
    m = 0
    if p < r :
        q = floor((p + r)/2)
        m1 = mergeSort(A, p, q)
        m2 = mergeSort(A, q+1, r)
        m3 = merge(A, p, q, r)
        m = m1 + m2 + m3
    return m

#insertion

def InsertionSort(A, a):
    o = 0
    for j in range (1, a):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
            o += 1
        A[i+1] = key
        o += 1
    return o



A = []
for j in range (1, 200):
    del A[:]
    A = []
    for i in range (1, j):
        A.append(i)
    shuffle(A)
    B = A
    C = A
    print(A)

    #quicksort
    n = quickSort(A, 0, len(A)-1)
    #print(A)


    #mergesort
    m = mergeSort(B, 0, len(B)-1)
    #print(B)

    #insertionsort
    o = InsertionSort(C, len(C))
    print(C)

    #print(n)
    #print(m)
    #print(o)
    print("Dla", j, "emelentow:")
    print("QuickSort zostal wykonany", n, "razy")
    print("MergeSort zostal wykonany", m, "razy")
    print("InsertionSort zostal wykonany", o, "razy")





