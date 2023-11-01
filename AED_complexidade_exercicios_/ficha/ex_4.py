import time

def naive(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    for letra in palavra1:
        if palavra1.count(letra) != palavra2.count(letra):
            return False
    return True

def ordenacao(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    return sorted(palavra1) == sorted(palavra2)

def bruteforce(palavra1, palavra2):
    def p_recursiva(s):
        if len(s) <= 1:
            return [s]
        perms = []
        for i, c in enumerate(s):
            for perm in p_recursiva(s[:i] + s[i+1:]):
                perms.append(c + perm)
        return perms

    if len(palavra1) != len(palavra2):
        return False
    return palavra2 in p_recursiva(palavra1)

def contagem(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    contagem_letras1 = {}
    contagem_letras2 = {}
    for letra in palavra1:
        contagem_letras1[letra] = contagem_letras1.get(letra, 0) + 1
    for letra in palavra2:
        contagem_letras2[letra] = contagem_letras2.get(letra, 0) + 1
    return contagem_letras1 == contagem_letras2

palavra1 = "amor"
palavra2 = "mora"

metodos = ['Naive', 'Ordenacao', 'Bruteforce', 'Contagem']

for metodo in metodos:
    inicio = time.time()
    if metodo == 'Naive':
        resultado = naive(palavra1, palavra2)
    elif metodo == 'Ordenacao':
        resultado = ordenacao(palavra1, palavra2)
    elif metodo == 'Bruteforce':
        resultado = bruteforce(palavra1, palavra2)
    elif metodo == 'Contagem':
        resultado = contagem(palavra1, palavra2)
    fim = time.time()
    tempo_decorrido = fim - inicio
    print(f"Método: {metodo}, Anagramas: {resultado}, Tempo: {tempo_decorrido} segundos")