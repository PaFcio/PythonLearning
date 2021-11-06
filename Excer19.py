# Przykład na continue

for num in range(1, 20):
    if not num % 2:  # num % 2 == 0
        print('Kolejna liczba parzysta:', num)
        continue
    print('Kolejna liczba:', num)
