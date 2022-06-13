import numpy as np

def utworz():
    polaczenia = np.array([[0,1,0],[0,0,1],[1,0,0]])
    pol_rozmiar = polaczenia.shape
    koszt = np.array([[0,3,0][0,0,6][2,0,0]])
    koszt_rozmiar = koszt.shape
    nazwa = ["A", "B", "C"]
    graf = [polaczenia, koszt, nazwa]
    eksport = [graf, pol_rozmiar, koszt_rozmiar]
    return eksport

if __name__ == "__main__":

        

