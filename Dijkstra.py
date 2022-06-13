import numpy as np
import copy

def sprawdzenie(A):
    if len(A) != 2:
        raise RuntimeError("Graf zawiera ilosc elementow inna niz 2")
    rozmiarPol = A[0].shape
    if len(A[1]) != rozmiarPol[0]:
        raise RuntimeError ("Zla ilosc nazw wezlow")
    return True

class Djikstra():
    def __init__(self, GRAF, start):
        self.wezly = GRAF[1]
        self.wagi = GRAF[0]
        self.wynik = np.zeros((len(self.wezly), len(self.wezly)))   
        self.pomoc = np.full((3, len(self.wezly)), None)            
        for i in range(len(self.wezly)):
            self.pomoc[1][i] = float('inf')                        
        self.start = self.wezly.index(start)                       
        self.pomoc[0][self.start] = 'empty'                            
        self.pomoc[1][self.start] = 0
        self.pomoc[2][self.start] = self.start
    
    def djikstra(self):                 
        self.szukaj(self.start)
        self.nanies()
        print(self.wynik)

    def nanies(self):                                                        
        for i in range(len(self.wezly)):
            self.wynik[self.pomoc[2][i]][i] = self.wagi[self.pomoc[2][i]][i]                

    def szukaj(self, wezel):
        self.pomoc[0][wezel] = 'empty'                                                                                     
        if None in self.pomoc[0]:                                                                                      
            for i in range(len(self.wagi)):                                                                            
                if ((self.pomoc[1][wezel] + self.wagi[wezel][i]) < self.pomoc[1][i]) and self.wagi[wezel][i] != 0:      
                    self.pomoc[1][i] = (self.pomoc[1][wezel] + self.wagi[wezel][i])                                     
                    self.pomoc[2][i] = wezel                                                                            
            minimum = float('inf')                                                                                     
            for j in range(len(self.wagi)):                                                                           
                if (self.pomoc[1][j] < minimum) and (self.pomoc[0][j] != 'empty'):
                    self.nast = copy.copy(j)                                                                           
                    minimum = copy.copy(self.pomoc[1][j])                                                             
            self.szukaj(self.nast)                                                                                      

def start(A):
    for i in range (0 , len(A[1])):
       print(A[1][i]) 
    z = input("Wprowadz nazwe grafu wejsciowego: ")
    for i in range (0 , len(A[1])):
        if z == A[1][i]:
            n = i+1  
    if not n or n == "0":
        raise RuntimeError("Niepoprawna nazwa grafu wejsciowego")
    n = n-1
    graf = Djikstra(A, A[1][n])
    graf.djikstra()


B = [np.array([[0, 5, 2, 0, 0, 0], [8, 0, 3, 7,0,0], [5, 3, 0, 7, 4, 0], [0, 2, 3, 0, 5, 6], [0, 0, 5, 4, 0, 2], [0, 0, 0, 9, 4, 0]]), ["one", "two", "three", "four", "five", "six"]]
sprawdzenie(B)
start(B)