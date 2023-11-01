import random


def minimoQuadratico():
    n = int(input("Quantos números quer na lista?"))
    lista = []

    for _ in range(n):
        numero_aleatorio = random.randint(1, 100)
        lista.append(numero_aleatorio)

    minimo = lista[0]
    for e in lista:
        for f in lista:
            if e < f and e < minimo:
                minimo = e
    return minimo
