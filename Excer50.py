# Otwórz plik i podaj pozycję

fo = open("text.txt", "r")
print("Nazwa pliku: ", fo.name)

pos = fo.tell()
print("Aktualna pozycja: {}".format(str(pos)))

line = fo.readline()
print("Czytaj linię: >" + line + "<")

line = fo.readline()
print("Czytaj linię: >" + line + "<")

pos = fo.tell()
print("Aktualna pozycja: {}".format(str(pos)))

# Zamknij otwarty plik
fo.close()