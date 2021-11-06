# Integer
i = 2
print(type(i))

# Floating point
f = 2.71828
print(type(f))

# Complex no.
c = 0.5 + 1j
print(type(c))

# Type conversion
print(float(i), '&', int(f), '&', c)

# Boolean
a = 2 > 1
print(a)
print(type(a))

# String
znak = 'A'
print(znak)
print(type(znak))

napis = "Ala ma kota"
print(napis[0])

# HERE IMPORTANT, HAS NOT ONLY START & STOP BUT ALSO STEP!!!
print(napis[0::2])

napis = "Ala ma koty"
print(napis)

zmienna = 127
print(zmienna)
print(type(zmienna))

zmienna = '127'
print(zmienna)
print(type(zmienna))

zmienna = '127'*127
print(zmienna)

napis = 'Ala ma kota a kot ma psa'
l_calk = 2
# print(napis + l_calk) tak nie można bo jest Str * Int

# Konwersja Int -> Str
print(napis + ' ' + str(l_calk))
