# Biorąc pod uwagę 2 ciągi, s1 i s2, utwórz nowy ciąg, dodając s2 w środku s1
s1 = "FullStack"
s2 = "Python"
slen = int(len(s1) / 2)
s3 = s1[:slen] + s2 + s1[slen:]
print(s3)
