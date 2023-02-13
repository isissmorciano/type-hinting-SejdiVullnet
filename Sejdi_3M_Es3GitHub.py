import random

def casuale(nome, eta):
    return nome, 'ha', eta, 'anni.'
eta=random.randint(0,99)
nome=str(input("inserisci il tuo nome: "))
print(casuale(nome, eta))