# Silnia x

def silnia(x):
    if x == 0:
        return 1
    else:
        return x * silnia(x - 1)


sil = int(input('Podaj liczbę do silni: '))
print(silnia(sil))
