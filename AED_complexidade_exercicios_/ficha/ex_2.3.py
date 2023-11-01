import random

def minimosimples():
    n = int(input("Quantos números quer na lista?"))
    lista = []

    for _ in range(n):
        numero_aleatorio = random.randint(1, 100)
        lista.append(numero_aleatorio)

    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num

    return minimo