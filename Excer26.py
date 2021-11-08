# Napisz funkcję w Pythonie, który zsumuje wszystkie elementy na liście.

def sum_list(my_list):
    sum = 0
    for el in my_list:
        sum += el
    return sum


in_list = []
val = input('Podaj element do listy: ')

while val != '':
    in_list.append(int(val))
    val = input('Podaj element do listy: ')

print(sum_list(in_list))
