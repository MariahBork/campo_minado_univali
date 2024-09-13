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
    return mapa

# Implementar do jeito da Bea
def exibirMapa(mapa):
    for i in mapa:
        print(i)