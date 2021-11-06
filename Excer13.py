# Utwórz listę zawierającą imiona wszystkich kursantów
# Następnie ją posortuj alfabetycznie, oraz policz ile z osób na liście jest kobietami
# W tym celu możesz sprawdzić czy imię kończy się na „a”

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
count = 0

for kurstant in kursanci:
    if kurstant[-1] == 'a':
        print('Kursantka ' + kursanci[kursanci.index(kurstant)] + ' jest kobietą')
        count = count + 1
    else:
        print('Kursant ' + kursanci[kursanci.index(kurstant)] + ' jest mężczyzną')

print('Ilość kobiet wśród kursantów to: ' + str(count))
