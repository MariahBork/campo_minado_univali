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
    run, matriz[linha][coluna] = func.revelarEspaco(mapa, linha, coluna)
print("Game Over")