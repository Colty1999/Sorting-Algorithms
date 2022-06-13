from random import shuffle

def InsertionSort(A, a):
    for j in range (1, a):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

A = []
for i in range (1, 150):
    A.append(i)
shuffle(A)
print(A)
InsertionSort(A, len(A))
print(A)

