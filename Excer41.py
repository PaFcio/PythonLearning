# Podziel przez siebie dwie liczby
# Umieść:
# wynik = "Nie możesz podzielić przez 0"
# we właściwym miejscu, aby program uniknął ZeroDivisionError
# Podpowiedź 1: Po prostu umieść przypisanie wartości dla wyniku po linii Except
# Podpowiedź 2: Zwróć uwagę na wcięcia

def dzielenie():

    l1 = input("Podaj liczbę 1: ")
    l2 = input("Podaj liczbę 2: ")
    l1 = int(l1)
    l2 = int(l2)

    try:
        l1 / l2
    except ZeroDivisionError:
        print("Nie możesz podzielić przez 0")
        dzielenie()
    else:
        print("Wynik to: " + str(l1 / l2))


dzielenie()
