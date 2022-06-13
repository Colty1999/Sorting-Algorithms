import numpy as np

def sprawdzenie(A):
    if len(A) != 3:
        raise RuntimeError("Graf zawiera ilosc elementow inna niz 3")
    rozmiarPol = A[0].shape
    rozmiarWag = A[1].shape
    if rozmiarPol != rozmiarWag :
        raise RuntimeError("Macierze połączeń i wag nie mają takich samych rozmiarów")
    if set(A[0].reshape(-1).tolist()) != set([1]) and set(A[0].reshape(-1).tolist()) != set([0,1])and set(A[0].reshape(-1).tolist()) != set([0]):
        raise RuntimeError("Macierz połączeń zawiera inną wartość niż 0 i 1")
    if len(A[2]) != rozmiarPol[0]:
        raise RuntimeError ("Zla ilosc nazw wezlow")
    return True
    
def DodawaniePolaczenia(A, z, do):
    indeksZ = A[2].index(z)
    indeksDO = A[2].index(do)
    A[0][indeksZ, indeksDO] = 1
    #A[1][indeksZ, indeksDO] = waga

def Stan(A):  
    graf1 = A[2].copy()
    graf1.insert(0, " ")
    graf2 = np.column_stack((A[2], A[0]))
    grafS1 = np.append([graf1], graf2, axis = 0)
    graf3 = np.column_stack((A[2], A[1]))
    grafS2 = np.append([graf1], graf3, axis = 0)
    print("POLACZENIA: \n", grafS1, "\n")
    print("WAGI \n", grafS2)
    
def wykonczeniowka(A):
    for a in range (0, A[0][0].size):
        for b in range (0, A[0][0].size):
            if A[0][a][b] == 1 and A[0][b][a] == 1:
                x = C[a][b]
                y = C[b][a]
                if x < y:
                    B[0][b][a] = 0
                else:
                    B[0][a][b] = 0

def dzialanie(A):
    y, a, b = 1000, 0, 0
    for i in range (0, A[1][0].size):
        A[1][i][i] = 0
        for j in range (0, A[1][0].size):
            x = A[1][i][j]
            if x < y and x != 0:
                y, a, b = x, i, j
    A[1][a][b] = 0
    if a != 0 or b!= 0 :
        DodawaniePolaczenia(A, A[2][a], A[2][b])
    wykonczeniowka(A)
    


B = [np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), np.array([[5, 5, 2],[8, 1, 3], [5, 3, 2]]), ["one", "two", "three"]]
C = B[1].copy()
sprawdzenie(B)
B[0]=np.zeros((len(B),len(B)))
for i in range (0 , B[1].size):
    dzialanie(B)
B[1]=C
print(B)
#print(C)


