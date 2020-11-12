import json

with open('moedas.json') as moedaarq:
    arq_analise = json.load(moedaarq)
    print(arq_analise['moeda'])