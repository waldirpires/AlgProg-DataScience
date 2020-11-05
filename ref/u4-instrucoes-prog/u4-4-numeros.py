def ehDivisivelPor(n, p):
    return n % p == 0

a = input('Digite o limite inferior: ')

b = input('Digite o limite superior: ')

c = input('Digite o 1o divisor: ')

d = input('Digite o 2o divisor: ')

for n in range(int(a), int(b)+1):
    if ehDivisivelPor(n, int(c)) and ehDivisivelPor(n, int(d)):
        print(n, c, d)