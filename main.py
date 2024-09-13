import functions as func
import numpy as np

arrayMapas = func.criarArrayMapas(3)
mapaEscolhido = func.mapaAleatorio(arrayMapas)
arquivo = open(f"./mapas/{str(mapaEscolhido)}.txt", "r")

mapa = func.criarMapa(arquivo)

func.exibirMapa(mapa)

#for row in mapa:
#    print(' '.join(map(str,row)))