import numpy as np

def sprawdzenie(A):
    if len(A) != 2:
        raise RuntimeError("Graf zawiera ilosc elementow inna niz 2")
    rozmiarPol = A[0].shape
    if len(A[1]) != rozmiarPol[0]:
        raise RuntimeError ("Zla ilosc nazw wezlow")
    return True
    
def szuk_sciezki(A,n,m, visited, road, point, parent):
    
    visited[n] = True
    road[point] = n
    point += 1

    for i in range (0, len(A[1])):
        if visited[i] == False and A[0][n][i] > 0 :
            parent[i] = n
            visited[i] = True
            u = i
            szuk_sciezki(A, u ,m, visited, road, point, parent)
    
    return True if visited[m] else False

def FordFulkerson(A, n, m):

        parent = [-1] * (len(A[1]))

        max_flow = 0
        visited = [False] * len(A[1])
        road = np.empty([len(A[1])])
        while szuk_sciezki(A,n,m, visited, road, 0, parent):

            path_flow = float("Inf")
            s = m
            while s != n:
                path_flow = min(path_flow, A[0][parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = m
            while(v != n):
                u = parent[v]
                A[0][u][v] -= path_flow
                A[0][v][u] += path_flow
                v = parent[v]
            parent = [-1] * (len(A[1]))
            visited = [False] * len(A[1])
            road = np.empty([len(A[1])])

        return max_flow




def start(A):
    for i in range (0 , len(A[1]) - 1):
       print(A[1][i]) # wypisz nazwy grafow
    z = input("Wprowadz nazwe grafu wejsciowego: ")
    for i in range (1 , len(A[1])):
        if z == A[1][i-1]:
            n = i   
    y = input("Wprowadz nazwe grafu wyjsciowego: ")
    for i in range (1 , len(A[1])):
        if y == A[1][i-1]:
            m = i
    if not n or n == "0":
        raise RuntimeError("Niepoprawna nazwa grafu wejsciowego")
    if not m or m == "0":
        raise RuntimeError("Niepoprawna nazwa grafu wyjsciowego")
    if n == m:
        raise RuntimeError("Sciezka prowadzi do tego samego grafu")
    n, m = n-1, m-1
    print (FordFulkerson(A, n, m))
     


    

B = [np.array([[0, 5, 2, 0, 0, 0], [8, 0, 3, 7,0,0], [5, 3, 0, 7, 4, 0], [0, 2, 3, 0, 5, 6], [0, 0, 5, 4, 0, 2], [0, 0, 0, 9, 4, 0]]), ["one", "two", "three", "four", "five", "six"]]
#B = [np.array([[0, 16, 13, 0, 0, 0], [0, 0, 10, 12, 0, 0], [0, 4, 0, 0, 14, 0], [0, 0, 3, 0, 0, 20], [0, 0, 0, 7, 0, 4], [0, 0, 0, 0, 0, 0]]), ['0', '1', '2', '3', '4', '5']]
sprawdzenie(B)
start(B)
#print(FordFulkerson(B, 0, 4))
#print(B)
