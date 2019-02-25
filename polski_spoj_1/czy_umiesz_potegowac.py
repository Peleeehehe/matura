a = int(input("Podstawa potegi: "))
b = int(input("Wykladnik potegi: "))

def power(a, b):
    x = a**b
    return x

def ostatnia(x):
    y = str(x)
    return y[len(y)-1]

def main():
    print(ostatnia(power(a, b)))

main()