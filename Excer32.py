# Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z danego łańcucha.
# Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
# Przykładowy ciąg : Python
# Oczekiwany wynik: Pyon
# Przykładowy ciąg : Py
# Oczekiwany wynik: PyPy
# Przykładowy ciąg : P
# Oczekiwany wynik: pusty ciąg

def ret_mangled_string(my_str):
    ret_str = ''
    if len(my_str) >= 2:
        ret_str = my_str[:2] + my_str[-2:]
    else:
        ret_str = ''
    return ret_str


in_str = str(input('Podaj ciąg wejściowy: '))
print(ret_mangled_string(in_str))
