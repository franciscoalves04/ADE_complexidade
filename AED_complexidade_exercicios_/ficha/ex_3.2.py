import time
from matplotlib import pyplot as plt
import random

def experiment_dic_get_set():
    tamanhos = [10, 100, 1000, 10000, 100000]
    tempos_get = []
    tempos_set = []

    for tamanho in tamanhos:
        dicionario = {str(i): random.randint(0, 100) for i in range(tamanho)}


        inicio_get = time.time()
        _ = dicionario.get('0')
        fim_get = time.time()
        tempo_get = fim_get - inicio_get
        tempos_get.append(tempo_get)

        chave = str(random.randint(0, tamanho))
        valor = random.randint(0, 100)
        inicio_set = time.time()
        dicionario[chave] = valor
        fim_set = time.time()
        tempo_set = fim_set - inicio_set
        tempos_set.append(tempo_set)

    plt.plot(tamanhos, tempos_get, label='get', marker='o')
    plt.plot(tamanhos, tempos_set, label='set', marker='x')
    plt.xlabel('Tamanho do Dicionário')
    plt.ylabel('Tempo (s)')
    plt.title('Complexidade das Operações de Get e Set em Dicionários')
    plt.legend()
    plt.show()

experiment_dic_get_set()

##o indece do get e set é de O(1) pois o tempo de acesso é sempre o mesmo independentemente do tamanho da lista