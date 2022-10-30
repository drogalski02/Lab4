# wyświetla czy liczba jest pierwsza
def liczbapierwsza(x):
    if x<2:
        print("Liczba jest mniejsza od 2 i nie jest pierwsza")
        return False
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            print("Liczba nie jest pierwsza")
            return False
    print("Liczba jest pierwsza")
    return True

print("Podaj liczbę: ")
x = int(input())
liczbapierwsza(x)