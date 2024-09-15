import functions as func
import numpy as np

arrayMapas = func.criarArrayMapas(3)
mapaEscolhido = func.mapaAleatorio(arrayMapas)
arquivo = open(f"./mapas/{str(mapaEscolhido)}.txt", "r")
mapa, tamanho = func.criarMapa(arquivo)
matriz = func.mapaUsuario(tamanho)

run = True

while(run):
    func.exibirMapa(matriz)
    linha = int(input("Insira a linha do espaço que deseja abrir: "))
    coluna = int(input("Insira a coluna do espaço que deseja abrir: "))
    linha-=1
    coluna-=1
    saida = func.revelarEspaco(mapa, linha, coluna, tamanho)
    if isinstance(saida[1],int):
        run, matriz[linha][coluna] = saida
    elif isinstance(saida[1], list):
        matriz[linha][coluna] = '-'
        booleano, lista = saida
        for pos in lista:
            x,y = pos
            matriz[x][y] = '-'
    else:
        run, matriz[linha][coluna] = saida
print("Game Over")