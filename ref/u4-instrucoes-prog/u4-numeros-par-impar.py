list = [0, 3, 6, 3, 2, 7, 11]

pares = []
impares = []

for n in list:
    print(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print('=')
print('Pares: ' , pares)
print('Impares: ' , impares)
