n = int(input("Podaj liczbe"))

def silnia(n):
    y = 1
    for x in range(1, n+1):
        y = y * x
    return y
def dwie_pierwsze(n):
    y = str(n)
    return(y[len(y)-1], y[len(y)-2])

def main():
    print(silnia(n))
    print(dwie_pierwsze(silnia(n)))
main()