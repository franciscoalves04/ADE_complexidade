import time
from matplotlib import pyplot as plt
from random import randint

def experimentação_lista_indice():
    tamanhos = [10, 100, 1000, 10000, 100000]
    tempos = []

    for tamanho in tamanhos:
        lista = [randint(0, 100) for _ in range(tamanho)]

        inicio = time.time()
        _ = lista[0]
        fim = time.time()

        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)

    plt.plot(tamanhos, tempos, marker='o')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Acesso')
    plt.title('Complexidade')
    plt.show()

experimentação_lista_indice()


##o indece é de O(1) pois o tempo de acesso é sempre o mesmo independentemente do tamanho da lista