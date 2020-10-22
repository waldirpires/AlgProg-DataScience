
# função
def ehPar(num):
    return num %2 == 0; # booleano

# entrada: número inteiro digitado pelo usuário

num = input('Digite um número inteiro: ')

# saída: informar se o numero é par ou impar 

if int(num) % 2 == 0:
    print('O número ' + num + ' é PAR.')
else:
    print('O número ' + num + ' é ÍMPAR.')

print(ehPar(12))    
print(ehPar(27))    