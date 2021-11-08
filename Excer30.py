# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów.
# Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# Oczekiwany wynik: 2

def count_start_end_string(my_list):
    count = 0
    for el in my_list:
        if el[0] == el[-1] and len(el) >= 2:
            count += 1
    return count


in_list = []
val = input('Podaj element do listy: ')

while val != '':
    in_list.append((val))
    val = input('Podaj element do listy: ')

print(count_start_end_string(in_list))
