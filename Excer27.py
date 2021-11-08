# Napisz funkcję w Pythonie, który mnoży wszystkie elementy na liście.

def multiply_list(my_list):
    wynik = my_list[0]
    for el in my_list[1:]:
        if el == 0:
            wynik = 0
            break
        wynik *= el
    return wynik


in_list = []
val = input('Podaj element do listy: ')

while val != '':
    in_list.append(int(val))
    val = input('Podaj element do listy: ')

print(multiply_list(in_list))
