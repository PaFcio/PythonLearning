# Liczby pierwsze - przykład na break w pętli for

for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n, 'jest liczbą pierwszą')
