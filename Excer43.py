# Spróbuj dodać int do ciągu.
# Umieść:
# msg = "Nie możesz dodać int do string"
# aby program uniknął błędu BaseException.
# Możesz użyć wyjątku Exception, chociaż zwykle powinno się ostrożnie używać tak potężnych instrukcji wyjątków.

l1 = int(input("Podaj liczbę 1: "))
str1 = input("Podaj ciąg 1: ")
msg = "Nie możesz dodać int do string"

try:
    l1 + str1
except Exception:  # Zbyt szeroka klauzula wyjątku na tę sytuację. Powwino być TypeError
    print(msg)

# else:
#    pass
