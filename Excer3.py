# Biorąc pod uwagę 2 ciągi: s1 i s2 zwróć nowy ciąg złożony z pierwszego,
# środkowego i ostatniego znaku każdego ciągu wejściowego

s1 = "America"
s2 = "Japan"
s1_len = int(len(s1)/2)
s2_len = int(len(s2)/2)
s3 = (s1[0] + s2[0] + s1[s1_len] + s2[s2_len] + s1[-1] + s2[-1])
print(s3)
