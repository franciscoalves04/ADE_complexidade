from complexidade_pack.complexidade import f_complexidade, f_complexidade_boxplot
from tempo_pack.tempo import f_tempo, f_boxplot


def faturial(n):
    total = 1
    for i in range(1, n+1):
        total = total * i
    return total


#####-----f_tempo-----#####
tempos_execucao, tempo_medio, desvio_padrao = f_tempo(faturial, 30, 10000)

print(tempos_execucao)
print(tempo_medio)
print(desvio_padrao)

#####-----Boxplot-----#####
a = f_boxplot([tempos_execucao])
print(a)

#####-----f_complexidade-----#####
dic_stats, dic_tempos = f_complexidade(faturial,[30,70,120,300],7)
print(dic_stats,dic_tempos)

#####-----f_complexidade_boxplot-----#####
c = f_complexidade_boxplot(dic_tempos)
print(c)