# Napisz funkcję w Pythonie, który zlicza liczbę znaków (częstotliwość znaków) w ciągu.
# Przykładowy ciąg : google.com
# Oczekiwany wynik : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def char_repetition(my_str):
    result_dict = {}
    for char in my_str:
        curr_keys = result_dict.keys()
        if char in curr_keys:
            result_dict [char] += 1
        else:
            result_dict [char] = 1
    return result_dict

in_str = input('Podaj ciąg wejściowy: ')
print(char_repetition(in_str))
