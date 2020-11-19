print('APCD - U7 - Calculadora\n')

print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão\n')

try:

    op = input('Digite sua opção: ')

    if op < '1' and op > '4':
        raise AssertionError('Opção inválida: {}'.format(op))

    a = float(input('digite o 1o valor: '))

    b = float(input('digite o 2o valor: '))

    c = 0.0

    if op == '1':
        op = ' + '
        c = a + b
    elif op == '2':
        op = ' - '
        c = a - b
    elif op == '3':
        op = ' * '
        c = a * b
    elif op == '4':
        op = ' / '
        c = a / b

    print('Resultado: {} {} {} = {}'.format(a, op, b, c))

except ZeroDivisionError:
    print('Divisão por zero não permitida.')
except TypeError:
    print('Valor informado com tipo inválido')
except AssertionError as e:
    print(e)
except:
    print('Erro inesperado')
else:
    print('\nPrograma concluído com sucesso.\n')
finally:
    print('\nPrograma encerrado (finally)\n')