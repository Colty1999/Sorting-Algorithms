from random import shuffle
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


A = []
for i in range (1, 150):
    A.append(i)
shuffle(A)
print(A)
n = quickSort(A, 0, len(A)-1)
print(A)
print("Petla zostala wykonana", n, "razy")