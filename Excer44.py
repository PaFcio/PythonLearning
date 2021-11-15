# Stwórz trójelementową listę.
# Spróbuj wydrukować piąty element.
# Umieść:
# msg = "Jesteś poza zakresem listy"
# aby uniknąć wyjątku IndexError.

my_list = []
element = 0

for el in range(1, 4):
    element = int(input("Podaj element: "))
    my_list.append(element)

try:
    print(my_list[4])
except IndexError as x:
    print("Jesteś poza zakresem listy! Błąd: " + str(x))

