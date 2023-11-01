import time
from matplotlib import pyplot as plt
import random


def experiment_del_list_dict():
    tamanhos = [10, 100, 1000, 10000, 100000]
    tempos_del_list = []
    tempos_del_dict = []

    for tamanho in tamanhos:
        lista = [random.randint(0, 100) for _ in range(tamanho)]

        inicio_del_list = time.time()
        del lista[0]
        fim_del_list = time.time()
        tempo_del_list = fim_del_list - inicio_del_list
        tempos_del_list.append(tempo_del_list)

        dicionario = {str(i): random.randint(0, 100) for i in range(tamanho)}

        chave = '0'
        inicio_del_dict = time.time()
        del dicionario[chave]
        fim_del_dict = time.time()
        tempo_del_dict = fim_del_dict - inicio_del_dict
        tempos_del_dict.append(tempo_del_dict)

    plt.plot(tamanhos, tempos_del_list, label='del em lista', marker='o')
    plt.plot(tamanhos, tempos_del_dict, label='del em dicionário', marker='x')
    plt.xlabel('Tamanho da Estrutura de Dados')
    plt.ylabel('Tempo (s)')
    plt.title('Desempenho do Operador del em Listas e Dicionários')
    plt.legend()
    plt.show()


experiment_del_list_dict()

#listas del: O(n)tempo aumenta linearmente com o tamanho da lista.
#dicionários del: O(1) - tempo constante e independente do tamanho do dicionário.