# Biorąc pod uwagę ciąg o nieparzystej długości większej niż 7,
# zwróć łańcuch złożony z trzech środkowych znaków danego ciągu:

str1 = "Datatypes"
st_len = len(str1)
mid_ind = int(st_len/2)
print(str1[mid_ind-1:mid_ind+2])
