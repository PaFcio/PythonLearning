# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# W tym celu użyj operatora % oraz pętli for

l1 = int(input('Podaj liczbę 1: '))
l2 = int(input('Podaj liczbę 2: '))

l_max = max(l1, l2)
l_min = min(l1, l2)
# print(l_max)


for num in range(l_min, 0, -1):
    if l1 % num == 0 and l2 % num == 0:
        print(num)
        break
