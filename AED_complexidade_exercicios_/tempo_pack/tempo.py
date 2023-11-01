import time
import statistics
from matplotlib import pyplot as plt

def f_tempo(funcao, entrada, n_vezes):
    tempos_execucao = []

    for _ in range(n_vezes):
        inicio = time.time()
        resultado = funcao(entrada)
        fim = time.time()
        tempo_execucao = fim - inicio
        tempos_execucao.append(tempo_execucao)

    tempo_medio = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)

    return tempos_execucao, tempo_medio, desvio_padrao

def f_boxplot(lista):
    plt.boxplot(lista)
    plt.xlabel('valor do input n da função f(n)')
    plt.ylabel('tempo de execução da função f(n) [s]')
    plt.title("Estudo da variabilidade do tempo de execução\n da função f para o valor n")

    return plt.show()
