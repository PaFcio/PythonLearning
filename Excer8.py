# Przypisz 8 do zmiennej x i 15 do zmiennej y
# Utwórz 2 instrukcje warunkowe
# Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”, jeśli x jest większe niż 3 lub y jest parzyste
# Niech drugi wypisze „Żaden warunek nie jest spełniony”, jeśli x jest mniejsze lub równe 3, a y jest nieparzyste
# Zmień wartości przypisane do x i y i ponownie uruchom komórkę, aby sprawdzić, czy kod nadal działa

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))

if x > 3 or y % 2 == 0:
    print('Co najmniej jeden z warunków jest spełniony')

if x <= 3 and y % 2 != 0:
    print('Żaden warunek nie jest spełniony')
