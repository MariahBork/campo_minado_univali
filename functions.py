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

def revelarEspaco(mapa, linha, coluna):
    if(mapa[linha][coluna] == 1):
        return False, "X"
    else:
        simbolo = verificarEspaco(mapa, linha, coluna)
        return True, simbolo
    
def verificarEspaco(mapa, linha, coluna):
    contador = 0
    array = [mapa[linha-1][coluna-1], mapa[linha-1][coluna], mapa[linha-1][coluna+1], mapa[linha][coluna-1], mapa[linha][coluna+1], mapa[linha+1][coluna-1], mapa[linha+1][coluna], mapa[linha+1][coluna+1]]
    for espaco in array:
        if(espaco == 1):
            contador+=1
    if(contador > 0):
        return contador
    else:
        return "-"