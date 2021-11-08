# Napisz program, policzy silnię dla liczby n tj.
# n! = 1*2*3*4...*(n-2)*(n-1)    *n
# Zrób to przez napisanie funkcji, która rekurencyjne będzie się odwoływała do samej siebie
# do momentu gdy będzie liczyła silnie dla 1, która wynosi 1.

def silnia(n):
    if n > 1:
        return silnia(n -1) * n
    else:
        return 1

in_n = int(input('Podaj zakres silni: '))
print(silnia(in_n))
