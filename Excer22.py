# Zamiana zmiennych

a = "Code Brainers"
b = 317
print('a = ' + str(a) + ' b = ' + str(b))
b, a = a, b
print('a = ' + str(a) + ' b = ' + str(b))

# Przykład na format
print("a: {}, b: {}".format(a,b))