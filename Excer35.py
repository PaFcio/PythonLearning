import sys

try:
    f = open("plik.txt")
    s = f.readline()
    i = int(s.strip())
    print(i)
except OSError as err:
    print("Błąd systemu: {0}".format(err))
except ValueError:
    print("Nie można dokonać konwersji.")
except:
    print("Nieoczekiwany wyjątek:", sys.exc_info()[0])
    raise