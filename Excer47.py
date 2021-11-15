# Napisz funkcję dzielącą jej argument pierwszy przez drugi.
# Spróbuj wykonać działanie i zwrócić wynik.
# W przypadku błędu dzielenia przez zero, wypisz komunikat o błędzie.
# Wypisz komunikat, który zawsze się wypisze.
# Wywołaj funkcję z różnymi argumentami.

def dzielenie(arg1, arg2):

    wynik = 0

    try:
        wynik = arg1 / arg2
        return wynik
    except ValueError:
        print("Podaj liczbę całkowitą!")
        arg1_except = int(input("Podaj liczbę 1: "))
        arg2_except = int(input("Podaj liczbę 2: "))
        dzielenie(arg1_except, arg2_except)
    except ZeroDivisionError as err:
        print("Błąd: {}. Błąd dzielenia przez 0! Podaj nowe liczby (bez 0)!".format(err))
        arg1_except = int(input("Podaj liczbę 1: "))
        arg2_except = int(input("Podaj liczbę 2: "))
        dzielenie(arg1_except, arg2_except)
    # else:
       # print("Wynik dzielenia to: {}".format(arg1 / arg2))
    finally:
        print("Program zakończony")


l1 = int(input("Podaj liczbę 1: "))
l2 = int(input("Podaj liczbę 2: "))
print(dzielenie(l1, l2))
