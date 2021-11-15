# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu i zapisze go na liście content_list.
# content_list to lista zawierająca przeczytane wiersze.
# Możesz skorzystać z podpowiedzi (podanej dalej).
# Podpowiedź
# Instrukcja with w Pythonie jest używana w obsłudze wyjątków, aby kod był czystszy i bardziej czytelny.
# Upraszcza zarządzanie wspólnymi zasobami, takimi jak strumienie plików.
# Zwróć uwagę na następujący przykład kodu, w jaki sposób użycie instrukcji with sprawia, że kod jest czystszy.

plik = "text.txt"
content_list = []

with open(plik, 'r') as file:
    content_list = file.readlines()

print(content_list)
