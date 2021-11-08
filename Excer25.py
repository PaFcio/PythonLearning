# Napisz funkcję w Pythonie do obliczania długości łańcucha

def chain(in_str):
    a = 0
    for num in in_str:
        a += 1
    return a


my_str = str(input('Podaj ciąg do sprawdzenia długości: '))
print(chain(my_str))
