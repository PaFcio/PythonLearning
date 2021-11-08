# Napisz funkcję w Pythonie, aby uzyskać największą liczbę z listy.

def max_in_list(my_list):
    max_val = my_list[0]
    for el in my_list[1:]:
        if el > max_val:
            max_val = el
    return max_val


in_list = []
val = input('Podaj element do listy: ')

while val != '':
    in_list.append(int(val))
    val = input('Podaj element do listy: ')

print(max_in_list(in_list))
