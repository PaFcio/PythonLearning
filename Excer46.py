# Użyj finally do zamykania obiektów i czyszczenia zasobów.
# Spróbuj otworzyć i zapisać (podpowiedź: write) w pliku, którego nie można zapisać.
# Zapewnij, aby program mógł kontynuować bez pozostawiania otwartego obiektu pliku.

import io

my_file = input("Podaj nazwę pliku: ")
f = ""

try:
    f = open(my_file, "w")
    f.write("Coś tam, coś tam")
except io.UnsupportedOperation:
    print("Cannot open the file!")
finally:
    f.close()
