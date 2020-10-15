'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém o loop principal de jogo
'''

from base import *	# importa todas as funções base
from random import shuffle as embaralhar	# importa a função de embaralhamento

# bandeira de jogo, caso False o programa finaliza
JOGO = True

# loop principal do jogo, quando acaba o jogo finaliza
while GAME:

	# criação do baralho imutável (referência somente)
	BARALHO = construir_baralhos(1)	# por enquanto só 1

	# bandeira de rodada, caso False a rodada termina
	RODADA = True

	# loop de rodada, quando acaba a rodada finaliza
	while RODADA:

		# --- --- PASSO 1 --- --- --- --- --- --- --- --- ---

		# *** definir apostas aqui ***

		# --- --- PASSO 2 --- --- --- --- --- --- --- --- ---
		# define o bolo de jogo a partir do baralho de
		# referência e embaralha as cartas
		bolo = list(BARALHO)
		embaralhar(bolo)

