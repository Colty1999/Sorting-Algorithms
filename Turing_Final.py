import numpy as np

# Maszyna Turinga do zamiany liczb binarnych na dziesietne. Obsluguje liczby o max 4 bitach.

class Turing:

    def __init__(self, lista, alfabet, stan):
        self.alfabet = alfabet      
        self.wskaznik = 0
        self.lista = lista
        self.stan = stan
        self.tasma()
        self.BinToDec()

    def tasma(self): 
        self.lista.insert(self.wskaznik, "#")
        self.przesun_wskaznik("R")
        self.lista.append("#")
        while self.lista[self.wskaznik] != "#":
           if self.lista[self.wskaznik] not in alfabet:
               del self.lista[self.wskaznik]
           else:
               self.przesun_wskaznik("R")  
        if self.wskaznik > 6:
            raise RuntimeError("tasma posiada wiecej bitow niz 4")
        self.przesun_wskaznik("P")
        self.przesun_wskaznik("K")
        while self.wskaznik != 4:
            self.przesun_wskaznik("P")
            self.lista.insert(self.wskaznik, 0)
            self.przesun_wskaznik("K")
        print("wprowadzona tasma")
        print(self.lista)
        self.przesun_wskaznik("P")

    def przesun_wskaznik(self, n):
        if n == "L":
            self.wskaznik -= 1      
        elif n == "R":
            self.wskaznik += 1 
        elif n == "P":
            self.przesun_wskaznik("L")
            while self.lista[self.wskaznik] != "#":
                self.przesun_wskaznik("L")
            self.przesun_wskaznik("R")
        elif n == "K":
            self.przesun_wskaznik("R")
            while self.lista[self.wskaznik] != "#":
                self.przesun_wskaznik("R")
            self.przesun_wskaznik("L")


    def usun_element(self):
        if self.lista[self.wskaznik-1] == "#" and self.stan == "start":
            self.lista[self.wskaznik] = "#"
            self.przesun_wskaznik("R")
            del self.lista[self.wskaznik-1]
        elif self.lista[self.wskaznik+1] == "#" and self.stan == "start":
            self.lista[self.wskaznik] = "#"
            del self.lista[self.wskaznik+1]
            self.przesun_wskaznik("L")
        else:
            del self.lista[self.wskaznik]

    def dodaj_element(self, wartosc):
        if self.lista[self.wskaznik] == "#" and self.wskaznik == -1:
            self.lista[self.wskaznik] = wartosc
            self.lista.append("#")
        elif self.lista[self.wskaznik] == "#" and self.wskaznik == 0:
            self.lista[self.wskaznik] = wartosc
            self.lista.insert(self.wskaznik,"#")
        else:
            self.lista.insert(self.wskaznik, wartosc)

    def BinToDec(self):

        if self.lista[self.wskaznik] == 0 and self.stan == "start" and self.wskaznik == 1:
            self.stan = "0"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 1 and self.stan == "start" and self.wskaznik == 1:
            self.stan = "1"
            self.przesun_wskaznik("R")

        if self.lista[self.wskaznik] == 0 and self.stan == "0" and self.wskaznik == 2:
            self.stan = "00"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 1 and self.stan == "0" and self.wskaznik == 2:
            self.stan = "01"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 0 and self.stan == "1" and self.wskaznik == 2:
            self.stan = "10"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 1 and self.stan == "1" and self.wskaznik == 2:
            self.stan = "11"
            self.przesun_wskaznik("R")

        if self.lista[self.wskaznik] == 0 and self.stan == "00" and self.wskaznik == 3:
            self.stan = "000"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 1 and self.stan == "00" and self.wskaznik == 3:
            self.stan = "001"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 0 and self.stan == "01" and self.wskaznik == 3:
            self.stan = "010"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 1 and self.stan == "01" and self.wskaznik == 3:
            self.stan = "011"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 0 and self.stan == "10" and self.wskaznik == 3:
            self.stan = "100"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 1 and self.stan == "10" and self.wskaznik == 3:
            self.stan = "101"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 0 and self.stan == "11" and self.wskaznik == 3:
            self.stan = "110"
            self.przesun_wskaznik("R")
        elif self.lista[self.wskaznik] == 1 and self.stan == "11" and self.wskaznik == 3:
            self.stan = "111"
            self.przesun_wskaznik("R")

        if self.lista[self.wskaznik] == 0 and self.stan == "000" and self.wskaznik == 4:
            self.stan = "0000"
        elif self.lista[self.wskaznik] == 1 and self.stan == "000" and self.wskaznik == 4:
            self.stan = "0001"
        elif self.lista[self.wskaznik] == 0 and self.stan == "001" and self.wskaznik == 4:
            self.stan = "0010"
        elif self.lista[self.wskaznik] == 1 and self.stan == "001" and self.wskaznik == 4:
            self.stan = "0011"
        elif self.lista[self.wskaznik] == 0 and self.stan == "010" and self.wskaznik == 4:
            self.stan = "0100"
        elif self.lista[self.wskaznik] == 1 and self.stan == "010" and self.wskaznik == 4:
            self.stan = "0101"
        elif self.lista[self.wskaznik] == 0 and self.stan == "011" and self.wskaznik == 4:
            self.stan = "0110"
        elif self.lista[self.wskaznik] == 1 and self.stan == "011" and self.wskaznik == 4:
            self.stan = "0111"
        elif self.lista[self.wskaznik] == 0 and self.stan == "100" and self.wskaznik == 4:
            self.stan = "1000"
        elif self.lista[self.wskaznik] == 1 and self.stan == "100" and self.wskaznik == 4:
            self.stan = "1001"
        elif self.lista[self.wskaznik] == 0 and self.stan == "101" and self.wskaznik == 4:
            self.stan = "1010"
        elif self.lista[self.wskaznik] == 1 and self.stan == "101" and self.wskaznik == 4:
            self.stan = "1011"
        elif self.lista[self.wskaznik] == 0 and self.stan == "110" and self.wskaznik == 4:
            self.stan = "1100"
        elif self.lista[self.wskaznik] == 1 and self.stan == "110" and self.wskaznik == 4:
            self.stan = "1101"
        elif self.lista[self.wskaznik] == 0 and self.stan == "111" and self.wskaznik == 4:
            self.stan = "1110"
        elif self.lista[self.wskaznik] == 1 and self.stan == "111" and self.wskaznik == 4:
            self.stan = "1111"

        if self.stan == "0000":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(0)
        elif self.stan == "0001":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(1)
        elif self.stan == "0010":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(2)
        elif self.stan == "0011":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(3)
        elif self.stan == "0100":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(4)
        elif self.stan == "0101":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(5)
        elif self.stan == "0110":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(6)
        elif self.stan == "0111":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(7)
        elif self.stan == "1000":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(8)
        elif self.stan == "1001":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(9)
        elif self.stan == "1010":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(1)
            self.przesun_wskaznik("R")
            self.dodaj_element(0)
        elif self.stan == "1011":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(1)
            self.przesun_wskaznik("R")
            self.dodaj_element(1)
        elif self.stan == "1100":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(1)
            self.przesun_wskaznik("R")
            self.dodaj_element(2)
        elif self.stan == "1101":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(1)
            self.przesun_wskaznik("R")
            self.dodaj_element(3)
        elif self.stan == "1110":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(1)
            self.przesun_wskaznik("R")
            self.dodaj_element(4)
        elif self.stan == "1111":
            self.przesun_wskaznik("P")
            while(self.lista[self.wskaznik] != "#"):
                self.usun_element()
            self.przesun_wskaznik("P")
            self.dodaj_element(1)
            self.przesun_wskaznik("R")
            self.dodaj_element(5)

    def druk(self):
        print (self.lista)


lista = [2,3,6,0,0,1,0,9]
alfabet = [0, 1]
stan = "start"
wynik = Turing(lista, alfabet, stan)
print("wynik:")
wynik.druk()




