# Podczas pisania funkcji najlepiej jest przeprowadzić walidację liczb.
# Jeśli użytkownicy wprowadzą tekst, pojawi się błąd podczas próby konwersji na int.
# Napisz program, który poprosi użytkownika o podanie dwóch liczb.
# Dodaj i wydrukuj wynik.
# Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.


def dodawanko():
    l1 = input("Podaj liczbę 1: ")
    l2 = input("Podaj liczbę 2: ")

    try:
        l1 = int(l1)
        l2 = int(l2)
    except:
        print("Jedna z liczb nie została podana, podaj obie liczby")
        dodawanko()
    else:
        print("Wynik dodawania to: " + str(l1 + l2))

dodawanko()
