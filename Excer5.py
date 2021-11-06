# Utwórz listę zawierającą imiona wszystkich kursantów
# Następnie ją posortuj alfabetycznie, oraz
# Sprawdź ile elementów ona zawiera (i wyprintuj obv)

kursanci = ['Anastazja',
            'Tomasz',
            'Magdalena',
            'Michał',
            'Paweł',
            'Paweł',
            'Elżbieta',
            'Joanna',
            'Michał',
            'Łukasz',
            'Kamil',
            'Marcin',
            'Jakub',
            'Natalia']

kursanci.sort()
print('Kurs ma ' + str(len(kursanci)) + ' kursantów i są to: ' + str(kursanci))

kursanci.reverse()

kursanci_sorted = sorted(kursanci)
print('Kurs ma ' + str(len(kursanci)) + ' kursantów i są to: ' + str(kursanci_sorted))
