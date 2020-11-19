print('APCD - U7 - Calculadora\n')

print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão\n')

op = input('Digite sua opção: ')

a = float(input('digite o 1o valor: '))

b = float(input('digite o 2o valor: '))

c = 0.0

if op == '1':
    c = a + b
elif op == '2':
    c = a - b
elif op == '3':
    c = a * b
elif op == '4':
    c = a / b

print('Resultado: ', c)