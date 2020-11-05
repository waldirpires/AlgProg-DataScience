str = 'teste'
print('Capitalize: ' + str.capitalize())

print('isUpper(): teste:' , 'teste'.isupper() , '\t Teste: ' , 'TESTE'.isupper())

print('islower(): teste:' , 'teste'.islower() , '\t Teste: ' , 'TESTE'.islower())

print('upper(): ' + 'teste'.upper())

print('count(): ', 'teste'.count('e'))

print('encode(): ' , 'teste'.encode())

print('find(): ', 'the book is on the table'.find('on'))

print('index(): ', 'the book is on the table'.index('on', 0, 18))

print('isalnum(): ', 'abc2'.isalnum(), '()*'.isalnum())

print('isalpha(): ', 'abc'.isalpha(), '()*'.isalpha())

print('isdecimal(): ', '128.2'.isdecimal(), '128'.isdecimal())

print('isnumeric(): ', '128.2'.isnumeric(), '128'.isnumeric())

print('isdigit(): ' , '128'.isdigit(), 'abc2'.isdigit())

print('lstrip(): ', len('    teste'.lstrip()))

print('join(): ', ' , '.join(['ab', 'cd', 'ef']))

print('partition(): ', 'the book is on the table'.partition(' '))

print('replace(): ', 'the book'.replace('o', 'a'))

print('rfind(): ', 'the book is on the table'.rfind('the'))

print('split(): ', 'the book is on the table'.split(' '))

print('splitlines(): ', 'the book is\non the table'.splitlines())

print('startswith(): ', 'the book is on the table'.startswith('this'))

print('endswith(): ', 'the book is on the table'.endswith('table'))

print('strip(): ', len('  teste  '.strip()))

print('swapcase(): ', ' ThE BooK'.swapcase())

print('title(): ', 'the book is on the table'.title());

print('zfill(): ', 'teste'.zfill(8))
