# Napisz program w Pythonie, aby odczytać i wyświetlić cały plik tekstowy.

f = open("text.txt", "r")
full_file = f.read()

print(full_file)
