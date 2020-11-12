import pickle

# objeto origem
frutas = ['Abacate', 'Banana', 'Maçã', 'Pera', 'Caqui', 'Goiaba', 'Laranja']

print('Lista: ', frutas)

#escrita
f = open('arq.bin', "wb")
pickle.dump(frutas, f)
f.close()

#leitura
f = open('arq.bin', "rb")
frutas2 = pickle.load(f)
f.close()

print("Lista: ", frutas2)

