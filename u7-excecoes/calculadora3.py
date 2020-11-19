
def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  return a * b

def divisao(a, b):
  return a / b

def exibirMenu():
    print('\nAPCD - U7 - Calculadora\n')

    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair\n')

op = '0'

while op != '5':

    try:
        exibirMenu()
        op = input('Digite sua opção: ')

        assert op >= '1' and op <= '5'

        if op == '5':
            break

        a = float(input('digite o 1o valor: '))

        b = float(input('digite o 2o valor: '))

        c = 0.0

        if op == '1':
            c = soma(a, b)
        elif op == '2':
            c = subtracao(a, b)
        elif op == '3':
            c = multiplicacao(a, b)
        elif op == '4':
            c = divisao(a, b)

        print('Resultado: ', c)

    except AssertionError:
        print('\n============================')
        print('Operação inválida!')

    except ValueError:
        print('\n============================')
        print('Valor informado deve ser um número!')

    except ZeroDivisionError:
        print('\n============================')
        print('Não é possível dividir por zero!')


print('\nObrigado pela preferência!\n')

# op | a | b | c
#  1 | 2 | 3 | 5
#  4 | 3 | 2 | 1.5
#  3 | 2 | 5 | 10.0