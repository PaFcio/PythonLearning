# KOlejny przykład na pętlę while

lines = list()
print('Wprowadź tekst po linijce.')
print('Żeby zakończyć wprowadź pustą linię.')
line = input('Następna linijka: ')
while line != '':
    lines.append(line)
    line = input('Następna linijka: ')  # reset
print(lines)
