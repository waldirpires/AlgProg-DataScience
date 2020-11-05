#concatenação
str_var = 'The book'
str_nova = str_var + ' is on the table'
print('concatenação:', str_nova)

#repetição
str = '#' * 10
print('repetição: ', str)

#comprimento
print('len(): ', len('the book is on the table'))

#capitalize
print('capitalize(): ', 'the book is on the table'.capitalize())

#count
carro = ['Gol','Gol','Palio','Uno','Uno','Gol','Fiesta','Fiesta','Fiesta','Gol']
print('count(): ', carro.count('Gol'))

#encode/decode
str = 'book'
encoded = str.encode()
decoded = encoded.decode()
print('encode/decode: ', str, '\tencoded: ', encoded,  '\tdecoded: ', decoded)
