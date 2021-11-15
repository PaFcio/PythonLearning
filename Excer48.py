# Użyj wszystkie 4 elementy struktury obsługi wyjątków przy otwieraniu plików.
# Spróbuj otworzyć do czytania plik.
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy.
# Na koniec zamknij ten plik.
# Jeżeli dany plik nie jest zamknięty (podpowiedź: f.closed), to go zamknij.

def opener(f):
    try:
        f = open(f)
    except FileNotFoundError:
        if f == "":
            quit("Program zakończony")
        else:
            print("Zadany plik nie istnieje! Podaj inny plik lub zatwierdź bez wartości by zakończyć:")
            f_else = input()
            opener(f_else)
    except IOError as err:
        print("{}. Nie można otworzyć pliku!".format(err))
    else:
        print("Plik o nazwie {} zawiera {} wierszy.".format(f, str(len(f.readline()))))
        f.close()
    finally:
        if f is open:
            f.close()


my_file = input("Podaj nazwę pliku: ")
opener(my_file)
