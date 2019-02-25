
l_liczb = int(input("Podaj ilosc liczb do sprawdzenia: "))
tab = []
for x in range(0, l_liczb):
    liczba = int(input())
    tab.append(liczba)

def isPrime(liczba):
    if(liczba == 2):
        return False
    elif(liczba == 1):
        return False
    else :
        for x in range(2, liczba):
            if(liczba%x == 0):
                return False
        return True

def main():
    for x in range(0, l_liczb):
        if(isPrime(tab[x])):
            print("TAK")
        else:
            print("NIE")

main()
