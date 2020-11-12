#abertura com try/catch:

path = '/home/wrpires/code/repos/newton-paiva-local/AlgProg-DataScience/u6-arquivos/'

try:
    f = open(path + "test.txt", encoding = 'utf-8')
    # perform file operations
    print(f.read())
    f.close()
finally:
    print('done')