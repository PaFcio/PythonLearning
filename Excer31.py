# Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku rosnącym
# według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
# Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def last_tuple(tuple):
    return tuple[-1]


def sort_tuple_list(my_list):
    return sorted(my_list, key=last_tuple)


in_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_tuple_list(in_list))
