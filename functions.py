import numpy as np
def criarArrayMapas(qnt):
    mapas = []
    for i in range(qnt):
        mapas.append(f"mapa{i+1}")
    return mapas

def mapaAleatorio(mapas):
    return np.random.choice(mapas)

def criarMapa(arquivo):
    tamanho = int(arquivo.readline().split()[0])
    mapa = []
    for linha in arquivo.readlines()[0:tamanho]:
        mapa.append([int(x) for x in linha.strip().split(" ")])
    return np.array(mapa), tamanho

def mapaUsuario(tamanho):
    matriz = np.full((tamanho, tamanho), "#")
    return matriz

def exibirMapa(matriz):
    for i in matriz:
        print(i)

def revelarEspaco(mapa, linha, coluna, tamanho):
    if(mapa[linha][coluna] == 1):
        return False, "X"
    else:
        simbolo = verificarEspaco(mapa, linha, coluna, tamanho)
        return True,simbolo
    
def verificarEspaco(mapa, linha, coluna, tamanho):
    contador = 0
    adj = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            newX, newY = linha + x, coluna + y
            if 0 <= newX < tamanho and 0 <= newY < tamanho and (x, y) != (0, 0):
                adj.append((newX, newY))
    for (x, y) in adj:
        if mapa[x][y] == 1:
            contador += 1
    return contador, adj

def verificarVitoria(matriz, tamanho):
    total = tamanho * tamanho
    bombas = tamanho - 1
    abertas = total - np.count_nonzero(matriz == '#')

    if abertas == total - bombas:
        return False, True
    else:
        return True, False
