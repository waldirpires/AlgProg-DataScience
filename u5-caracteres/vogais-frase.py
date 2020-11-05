
# entrada

frase = input('Digite uma frase: ')
vogais = 'aeiou'

count = 0
vogais = {}

# processamento
for vogal in vogais:
    count = frase.lower().count(vogal)
    vogais[vogal] = count
#    if frase.lower().count(vogal) > 0:
#       count = count + 1

# saída
#print('Vogais encontradas: ', count)
print(vogais)
