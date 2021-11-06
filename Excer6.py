# Napisz program, który:
# Będzie prosił użytkownika o podanie dwóch liczb, i
# Wypisze:
# Wynik ich dzielenia,
# Resztę z dzielenia, oraz
# Wynik dzielenia całkowitego

# Input na podanie liczby 1
l1 = float(input('Podaj liczbę 1: '))
# Input na podanie liczby 2
l2 = float(input('Podaj liczbę 2: '))

print('Wynik dzielenia to: ' + str(l1/l2))
print('Reszta z dzielenia całkowitego: ' + str(l1%l2))
print('Dzielenie całkowite :' + str(l1//l2))