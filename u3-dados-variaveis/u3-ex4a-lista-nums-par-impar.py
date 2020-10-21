
def ehPar(num):
    return num % 2 == 0


lista = [0, 3, 6, 2, 3, 6, 5, 7]

pares = []
impares = []

for num in lista:
    if (ehPar(num)):
        pares.append(num)
    else:
        impares.append(num)

print('\nPares: ')
print(pares)
print('\nImpares: ')
print(impares)
