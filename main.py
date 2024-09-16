import functions as func
import numpy as np

arrayMapas = func.criarArrayMapas(3)
mapaEscolhido = func.mapaAleatorio(arrayMapas)
arquivo = open(f"./mapas/{str(mapaEscolhido)}.txt", "r")
mapa, tamanho = func.criarMapa(arquivo)
matriz = func.mapaUsuario(tamanho)

run = True
vitoria = False

while(run):
    func.exibirMapa(matriz)
    linha = int(input("Insira a linha do espaço que deseja abrir: "))
    coluna = int(input("Insira a coluna do espaço que deseja abrir: "))
    linha-=1
    coluna-=1
    saida = func.revelarEspaco(mapa, linha, coluna, tamanho)
    saida_ = saida[1]
    if isinstance(saida_[0], str):
        run, matriz[linha][coluna] = saida
    else:
        if(saida_[0] > 0):
            run = saida[0]
            matriz[linha][coluna] = saida_[0]
        elif isinstance(saida_[1], list):
            matriz[linha][coluna] = '-'
            for pos in saida_[1]:
                cont_= 0
                x,y = pos
                matriz[x][y] = '-'
                cont = func.verificarEspaco(mapa,x,y,tamanho)
                cont_ = cont[0]
                if cont_ > 0:
                    matriz[x][y] = cont_
    run, vitoria = func.verificarVitoria(matriz, tamanho)
if(vitoria):
    print("Você venceu!")
else:
    print("Game Over")