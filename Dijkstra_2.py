import numpy as np
import copy             #ulubiona biblioteka rekurencji. WHY? w pythonie piszac a = b, a nie przybiera wartosci b, ale jest odwolaniem do niej. Przykład: b = 2...a = b...a = 2; ale jezeli teraz b = 3, to a = 3, a nie 2; zatem trzeba skopiowac wartosc b i przypisac ja bezposrednio do a. a = b.copy() lub a = copy.copy(b) w celu bezwzglednego skopiowania danych

#witam serdecznie z tej strony dżej dżej dżoker, subskrybujcie i polubcie mój film na fb plssss\
#wiem ze zachowuje sie jak Gonciarz

class Dixit():
    def __init__(self, GRAF, start):
        self.wezly = GRAF[1]
        self.wagi = GRAF[0]
        self.wynik = np.zeros((len(self.wezly), len(self.wezly)))   #WYNIK to nasza macierz wyjsciowa, na razie jest zlozona z samych zer
        self.pomoc = np.full((3, len(self.wezly)), None)            #POMOC to macierz skladajaca sie z 3 wierszy: 1 - wskaznik zatwierdzenia wezla, wystepuje przy nim X wowczas, cos jak pokolorowanie wezla na czarno u lopatki. 2-wartosc wezla/koszt dojscia do wezla. 3-nr indeksu wezla z ktorego nastapilo polaczenie do tego wezla. NA SAMYM POCZATKU JEST TO PUSTA MACIERZ Z ELEMENTAMI: None
        for i in range(len(self.wezly)):
            self.pomoc[1][i] = float('inf')                         #zamiana wszystkich wartosci wezlow na nieskonczonosc - funkcja porownania nie radzi sobie z łączeniem INT + None
        self.poczat = self.wezly.index(start)                       #nr indeksu startowego
        self.pomoc[0][self.poczat] = 'x'                            #dla indeksu startowego nasza macierz pomocnicza z automatu potiwerdza wezel i wstawia wartosc 0
        self.pomoc[1][self.poczat] = 0
        self.pomoc[2][self.poczat] = self.poczat
    
    def extra(self, wezel):
        self.pomoc[0][wezel] = 'x'                                                                                      #zatwierdzamy wezel, jezeli juz tutaj program sie znajdzie, tzn ze musial zostac wczesniej zatweirdzony wezel
        if None in self.pomoc[0]:                                                                                       #warunek konieczny do sprawdzenia: stopniowo w kazdej iteracji Pomoc[1] sie zatwierdza, jezeli nie ma None, metoda sie nie powtarza
            for i in range(len(self.wagi)):                                                                             #ogarnianie sasiedztwa i dodawanie wartosci do wezlow WSZYSTKICH
                if ((self.pomoc[1][wezel] + self.wagi[wezel][i]) < self.pomoc[1][i]) and self.wagi[wezel][i] != 0:      #do tego jest nam nieskocznosc potrzebna. Dzieki temu program nam wejdzie do kazdego wezla, gdyby bylo ustawione 0 na poczatku to nigdy nie nadpisalibysmy wartosci wezlow
                    self.pomoc[1][i] = (self.pomoc[1][wezel] + self.wagi[wezel][i])                                     #wartosc wezla = wczesniejszy wezel z ktorego zostalo wykonane polaczenie + wartosc polaczenia miedzy tymi wezlami
                    self.pomoc[2][i] = wezel                                                                            #zapisujemy here nr indexu wezla z ktorego ruszamy, jest to potrzebne aby moc naszkicowac macierz tylko z wymaganymi polaczeniami 
            minimum = float('inf')                                                                                      #minimum LOKALNE, sluzy do porownywania i wybrania najmniejszego wezla do ktorego next sie wybierzemy
            for j in range(len(self.wagi)):                                                                             #A WIEC TAK, wezły do ktorych mozemy sie wybrac to te juz sprawdzone^, ALE nie zatwierdzone, wiec warunki koneiczne: Pomoc[0] to nie X oraz Pomoc[1] < minimum (na poczatku min = inf, wiec warunek bedzie spelniony)
                if (self.pomoc[1][j] < minimum) and (self.pomoc[0][j] != 'x'):
                    self.nast = copy.copy(j)                                                                            #ze wzgledu, ze to jest rekurencja tej samej funkcji to musimy ustawic zmienna globalna ktora zapisuje wartosc indeksu nastepnego wezla az nie zostanie zmieniona
                    minimum = copy.copy(self.pomoc[1][j])                                                               #jw. ale zapisujemy minimum
            self.extra(self.nast)                                                                                       #rekurencyjnie wywolujemy ponownie funkcje, ale zaczynamy od nastepnego wezla

    def szkicowanie(self):                                                                  #funkcja szkicowanie nanosi wartosci z grafu wag w miejscach ustalonych w Pomoc[2] na nasz graf wynikowy (aktualnie same zera)
        for i in range(len(self.wezly)):
            self.wynik[self.pomoc[2][i]][i] = self.wagi[self.pomoc[2][i]][i]                #pogmatwane ale dziala, basically: w Pomoc[0:2] indeks kazdej kolumny to DOCELOWY wezel [i], a wartosc poszeczegolnej KOMORKI w Pomoc[2] to wezel z ktorego wychodzi polaczenie tj nr wiersza w grafie wynikowym;

    
    def dixit(self):                 #cos a la main(), wykonaj ogarniecie pomocy oraz naszkicuj graf z pomocy
        self.extra(self.poczat)
        self.szkicowanie()
        print(self.wynik)
        
#przyklad Lopatki nizej zapisany

#A = [np.array([[0, 10, 0, 5, 0],[0, 0, 1, 2, 0], [0, 0, 0, 0, 4], [0, 3, 9, 0, 2], [7, 0, 6, 0, 0]]), ['S', 'U', 'V', 'X', 'Y']]
A = [np.array([[0, 5, 2, 0, 0, 0], [8, 0, 3, 7,0,0], [5, 3, 0, 7, 4, 0], [0, 2, 3, 0, 5, 6], [0, 0, 5, 4, 0, 2], [0, 0, 0, 9, 4, 0]]), ["one", "two", "three", "four", "five", "six"]]
djixtra = Dixit(A, "one")

djixtra.dixit()

