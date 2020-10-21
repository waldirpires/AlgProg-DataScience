frase = input('Digite uma frase: ')

tamanho = len(frase)

print('\033[92m]=== forma 1 usando slicing\033[0m')

# começando em tamanho, terminar em zero, passo -1
sliced = frase[tamanho::-1]

print(sliced)

print('\033[92m]=== forma 2 usando vetor\033[0m')

inverso = []
while tamanho > 0:
    inverso += frase[tamanho-1]
    tamanho = tamanho - 1

print(inverso)

for a in inverso:
    print(a, end = '')

print()

print('\033[92m]=== forma 3 usando join\033[0m')
inverso = ''.join(reversed(frase))
print(inverso)