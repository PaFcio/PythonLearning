def fibonacci_numbers(n):
    """
    Zwraca liczby Fibonacciego mniejsze od n
    :param n:
    :return:
    """
    wynik = []
    a, b = 0, 1
    while a < n:
        wynik.append(a)
        a, b = b, a+b
    return wynik


def fibonacci_numbers2(n):
    """
    Zwraca liczby Fibonacciego po n-iteracjach
    :param n:
    :return:
    """
    wynik = []
    a, b = 0, 1
    while len(wynik) <= n:
        wynik.append(a)
        a, b = b, a+b
    return wynik


n_in = int(input('Podaj końcową liczbę ciągu Fibonacciego: '))
print(fibonacci_numbers(n_in))
print(fibonacci_numbers.__doc__)

print(fibonacci_numbers2(n_in))
print(fibonacci_numbers2.__doc__)
