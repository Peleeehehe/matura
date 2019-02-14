from auto import Auto
import csv
import os

clear = lambda: os.system('cls')

auta = []

#<editor-fold desc = "Funkcje">

def nowe_auto(a, b, c, d, e, f):
    x = Auto(a, b ,c ,d, e, f)
    auta.append(x)
    zapisz1(x)

def stworz_auto(a, b, c, d, e, f):
    x = Auto(a, b ,c ,d, e, f)
    auta.append(x)

def usun_auto():
    pokaz_auta()
    print("Ktore auto chcesz usunac?")
    index = int(input("Numer auta: "))
    del auta[index-1]
    print('\n')

def zmien_auto():
    print("Auta w systemie:")
    pokaz_auta()
    print("Ktore auto chcesz zmienic?")
    choice1 = int(input("Numer auta:"))
    print("Ktora wartosc chcesz zmienic?")
    choice2 = input("marka/model/przebieg/rocznik/imie/nazwisko")
    print("Podaj nowa wartosc:")
    choice3 = input()
    setattr(auta[choice1-1], choice2, choice3)
    print('\n')

def pokaz_auta():
    y = 1
    print("Aktualnie w systemie jest", len(auta)," aut.")
    print("Marka, Model, Przebieg, Rocznik, Imie i nazwisko wlasciciela")
    print('\n')
    for auto in auta:
        print(y,end='')
        print(".", end=' ')
        print(auto.marka, end=' ')
        print(auto.model, end=' ')
        print(auto.przebieg, end=' ')
        print(auto.rocznik, end=' ')
        print(auto.imie_wlasciciela, end=' ')
        print(auto.nazwisko_wlasciciela, end='\n')
        y+=1


def zapisz1(x):
    f = open('auta.txt', 'a')
    f.write('{};{};{};{};{};{}\n'.format(x.marka, x.model, x.przebieg, x.rocznik, x.imie_wlasciciela, x.nazwisko_wlasciciela))
    f.close()

def wczytaj_auta():
    tab = []
    with open('auta.txt', newline='') as f:
        garaz = csv.reader(f, delimiter= ';')
        for auto in garaz:
            nowe_auto = stworz_auto(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5])
            tab.append(nowe_auto)
    return tab
#</editor-fold>

def main():
    wczytaj_auta()
    while True:
        clear()
        print("Co chcesz zrobic?")
        print("1.Dodaj auto")
        print("2.Usun auto")
        print("3.Zmien auto")
        print("4.Pokaz auta")
        print("0.Koniec")
        choice = int(input())
        if(choice == 1):
            clear()
            print("Podaj marke, model, przebieg, rocznik, imie wlasciciela i nazwisko wlasciciela auta")
            a = input("Marka: ")
            b = input("Model: ")
            c = int(input("Przebieg: "))
            d = int(input("Rocznik: "))
            e = input("Imie wlasciciela: ")
            f = input("Nazwisko wlasciciela: ")
            nowe_auto(a, b, c, d, e, f)
        elif(choice == 2):
            clear()
            usun_auto()
        elif(choice == 3):
            clear()
            zmien_auto()
        elif(choice == 4):
            clear()
            pokaz_auta()
        elif(choice == 0):
            break

main()