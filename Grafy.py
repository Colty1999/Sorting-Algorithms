import numpy as np

def sprawdzenie(A):
    if len(A) != 3:
        raise RuntimeError("Graf zawiera ilosc elementow inna niz 3")
    rozmiarPol = A[0].shape
    rozmiarWag = A[1].shape
    if rozmiarPol != rozmiarWag :
        raise RuntimeError("Macierze połączeń i wag nie mają takich samych rozmiarów")
    if set(A[0].reshape(-1).tolist()) != set([0,1]):
        raise RuntimeError("Macierz połączeń zawiera inną wartość niż 0 i 1")
    if len(A[2]) != rozmiarPol[0]:
        raise RuntimeError ("Zla ilosc nazw wezlow")
    return True

def DodawanieWezla(A : list, dopisz : str):
    if dopisz in A[2]:
        raise RuntimeError("Wezel juz istnieje")
    A[2].append(dopisz)
    shape = A[0].shape
    matrices = [A[0], A[1]]
    for index, matrix in enumerate(matrices):
        new_matrix = np.zeros((shape[0]+1, shape[1]+1))
        new_matrix[:shape[0], :shape[1]] = matrix
        A[index] = new_matrix


def UsuwanieWezla(A : list, usun : str):
    if usun not in A[2]:
        raise RuntimeError("Wezel nie istneje")
    node_pos = A[2].index(usun)
    del A[2][node_pos]
    matrices = [A[0], A[1]]
    for index, matrix in enumerate(matrices):
        matrix = np.delete(matrix, node_pos, axis=0)
        A[index] = np.delete(matrix, node_pos, axis=1)


    
def DodawaniePolaczenia(A, waga, z, do):
    indeksZ = A[2].index(z)
    indeksDO = A[2].index(do)
    A[0][indeksZ, indeksDO] = 1
    A[1][indeksZ, indeksDO] = waga

def UsuwaniePolaczenia(A, z, do):
    indeksZ = A[2].index(z)
    indeksDO = A[2].index(do)
    A[0][indeksZ, indeksDO] = 0

def Stan(A):  
    graf1 = A[2].copy()
    graf1.insert(0, " ")
    graf2 = np.column_stack((A[2], A[0]))
    grafS1 = np.append([graf1], graf2, axis = 0)
    graf3 = np.column_stack((A[2], A[1]))
    grafS2 = np.append([graf1], graf3, axis = 0)
    print("POLACZENIA: \n", grafS1, "\n")
    print("WAGI \n", grafS2)
    

def Polaczenia(A, wezel):
    indeksW = A[2].index(wezel)
    sasiedztwo = []
    for i in range (0, len(A[0])):
        if A[0][indeksW][i] == 1:
            sasiedztwo.append(A[2][i])
    print(sasiedztwo)
    return sasiedztwo

def Wykonanie(A, funkcja):
    if funkcja == 1:
        if sprawdzenie(A) == True:
            print("Lista A jest grafem")
    elif funkcja == 2:
        dopisz = input("Podaj nazwe wezla do dodania \t")
        DodawanieWezla(A, dopisz)
    elif funkcja == 3:
        usun = input("Podaj nazwe wezla do usuniecia \t")
        UsuwanieWezla(A, usun)
    elif funkcja == 4:
        waga = input("Podaj wage polaczenia \t")
        z = input("Podaj nazwe wezla 'z' \t")
        do = input("Podaj nazwe wezla 'do' \t")
        DodawaniePolaczenia(A, waga, z, do)
    elif funkcja == 5:
        z = input("Podaj nazwe wezla 'z' \t")
        do = input("Podaj nazwe wezla 'do' \t")
        UsuwaniePolaczenia(A, z, do)
    elif funkcja == 6:
        Stan(A)
    elif funkcja == 7:
        wezel = input("Podaj nazwe \t")
        Polaczenia(A, wezel)
    else:
        print("Niepoprawny numer")
    print("Podaj kolejna funkcje")
    start(A)

def start(A):
    print("Funkcje:")
    print("   1 sprawdzenie(A) - sprawdza czy lista A jest grafem")
    print("   2 dodawanieWezla(A, nazwa_wezla) - dodaje wezel o podanej nazwie w liscie A")
    print("   3 usuwanieWezla(A, nazwa_wezla) - usuwa wezel o podanej nazwie w liscie A")
    print("   4 dodawaniePolaczenia(A, waga, z, do) - dodaje polaczenie SKIEROWANE miedzy dwoma wezlami")
    print("   5 usuwaniePolaczenia(A, z, do) - usuwa polaczenie SKIEROWANE miedzy dwoma wezlami")
    print("   6 Stan(A) - wyswietla graf połączeń w liscie A")
    print("   7 Polaczenia(A, wezel) - pokazuje wszystkie wezly, z ktorymi dany wezel ma polaczenia")
    funkcja = int(input("Prosze podac numer funkcji: \t"))
    Wykonanie(A, funkcja)
    

A = [np.array([[1, 0, 1], [0, 0, 1], [1, 0, 0]]), np.array([[0.5, 0, 2],[0, 0, 3], [5, 0, 0]]), ["one", "two", "three"]]
sprawdzenie(A)
start(A)
