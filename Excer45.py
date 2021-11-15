# Spróbuj otworzyć do czytania plik (podpowiedź: f = open(arg, "r")).
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy (podpowiedź: len(f.readlines()).
# Na koniec zamknij ten plik (podpowiedź: f.close()).

# arg = "readme2.txt"
arg = "Excer7.py"

try:
    f = open(arg, "r")
except FileNotFoundError:
    print("File not found! Filename: " + arg)
else:
    print("Plik {} ma {} wierszy".format(arg, len(f.readlines())))
    f.close()
