num = input('Digite um número inteiro: ')

print('Taboada de ' + num + '\n')

for n in range(0, 11):
    r = n * int(num)
    print(num, ' * ' , str(n) , ' = ' , str(r))