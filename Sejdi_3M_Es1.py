def lavoro(nome, eta):
    return nome, 'ha', eta, 'anni.'

nome=str(input("inserisci il tuo nome: "))
eta=int(input("Inserisci la tua età: "))
print(lavoro(nome, eta))
