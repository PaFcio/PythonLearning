# Rekurencyjny ciąg Fibonacciego w Pythonie.

def fibonacci(n):
    if n >= 2:
        return fibonacci(n-2) + fibonacci(n-1)
    else:
        return n


in_n = int(input('Podaj n: '))
print(fibonacci(in_n))
