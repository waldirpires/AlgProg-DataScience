import json

with open('teste.json') as f:
    arq = json.load(f)

print('Todo o JSON: ', arq)

print('Campo específico: ', arq['Cep'])