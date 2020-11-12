path = '/home/wrpires/code/repos/newton-paiva-local/AlgProg-DataScience/u6-arquivos/'

# escrita:
with open("test.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

print("\nLendo: \n")

with open("test.txt",'r',encoding = 'utf-8') as f:
    read = f.read()
    while (read != ''):
        print(read)
        read = f.read()