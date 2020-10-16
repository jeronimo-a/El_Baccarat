'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém o loop principal de jogo
'''

from base import *	# importa todas as funções base
from falas import falas	# importa as falas do jogo
from random import shuffle as embaralhar	# importa a função de embaralhamento

# bandeira de jogo, caso False o programa finaliza
JOGO = True

# loop principal do jogo, quando acaba o jogo finaliza
while JOGO:

	# fala de início de jogo
	print(falas['bandeiras']['inicio jogo'])

	# pergunta com quantos baralhos jogar, verificando erros
	numero_baralhos = solicitar_entrada(
		falas['numero baralhos'],
		'int', whitelist=[1,6,8]
		)

	# criação do baralho imutável (referência somente)
	BARALHO = baralhos(numero_baralhos)

	# pergunta quantas pessoas vão jogar, verificando erros
	numero_jogadores = solicitar_entrada(falas['numero jogadores'], 'int')

	# nomeação dos jogadores e atribuição de fichas 
	FICHAS = dict()	# FICHAS[nome_jogador] = fundos_jogador

	# pergunta o nome dos jogadores
	for n in range(1, numero_jogadores + 1):

		# solicita o nome dos jogadores, verificando erros
		nome = solicitar_entrada(
			falas['nomes'], 'str',
			blacklist=[''],
			variavel_pergunta=str(n),
			marcador_variavel=';'
			)

		# define quantidade de fichas do jogador
		FICHAS[nome] = 1000

	# bandeira de rodada, caso False a rodada termina
	RODADA = True

	# loop de rodada, quando acaba a rodada finaliza
	while RODADA:

		# fala de início de rodada
		print(falas['bandeiras']['inicio rodada'])

		# --- --- PASSO 1: APOSTAS --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

		# dicionario de apostas
		APOSTAS = dict()	# APOSTA[nome_jogador] = (quanto_aposta, qual_aposta)

		# loop de apostas por jogador
		for nome in FICHAS.keys():

			# pergunta qual é a aposta, verificando erros
			qual_aposta = solicitar_entrada(
				falas['qual aposta'], 'str',
				whitelist=['B', 'J', 'E'],
				variavel_pergunta=nome,
				marcador_variavel=';'
				)

			# pergunta quanto quer apostar, verificando erros
			quanto_aposta = solicitar_entrada(
				falas['quanto aposta'], 'int',
				maximo=FICHAS[nome],
				minimo=0
				)

			# gracinha
			if quanto_aposta == 0: print(nome, falas['tirar sarro']['sem aposta'])
			
			# registra a aposta
			APOSTAS[nome]= (qual_aposta, quanto_aposta)
			

		# --- --- PASSO 2: EMBARALHAR --- --- --- --- --- --- --- --- --- --- --- --- --- ---

		# define o bolo de jogo a partir do baralho de referência
		BOLO = list(BARALHO)

		# embaralha o bolo
		embaralhar(BOLO)







