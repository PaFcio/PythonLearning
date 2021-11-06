# Znajdź liczby, które są podzielne przez 7 i są wielokrotnością 5 w zakresie
# Napisz program w Pythonie,
# aby znaleźć liczby podzielne przez 7 i będące wielokrotnością 5 między 1500 a 2700 (obie uwzględnione)

l1 = 1500
l2 = 2700
wyniki = list()

for cur_l in range(l1, l2 + 1):
    if cur_l % 7 == 0 and cur_l % 5 == 0:
        wyniki.append(cur_l)

print(wyniki)
