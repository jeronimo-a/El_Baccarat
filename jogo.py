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
while JOGO:

	# loop que pergunta com quantos baralhos jogar
	while True:

		# pergunta
		numero_baralhos = input('Com quantos baralhos gostaria de jogar? (1, 6 ou 8)')

		# verifica se o input é um número
		try: numero_baralhos = int(numero_baralhos)

		except:
			print('Não entendi.')
			continue

		# verifica se o número é 1, 6 ou 8
		if numero_baralhos not in [1, 6, 8]:
			print('Não jogamos com essa quantidade de baralhos.')
			continue

		break


	# criação do baralho imutável (referência somente)
	BARALHO = construir_baralhos(numero_baralhos)


	# loop que pergunta o número de jogadores
	while True:

		# input do número de jogadores
		numero_jogadores = input('Quantas pessoas vão apostar?')

		# verifica se o valor é um número
		try: 
			numero_jogadores = int(numero_jogadores)
			break

		except:
			print('Não entendi.')
			continue 


	# nomeação dos jogadores e atribuição de fichas 
	FICHAS = dict()	# FICHAS[nome_jogador] = fundos_jogador


	# pergunta o nome dos jogadores
	for _ in range(1, numero_jogadores + 1):

		# loop de verificação de validade
		while True:

			# input do nome
			nome = input('Qual o nome do jogador %d?' % i, end=' ')

			# verifica se é uma string vazia
			if nome == '':
				print('Você tem que chamá-lo de algo.')
				continue

			# designa as fichas iniciais
			FICHAS[nome] = 1000


	# bandeira de rodada, caso False a rodada termina
	RODADA = True

	# loop de rodada, quando acaba a rodada finaliza
	while RODADA:

		# --- --- PASSO 1: APOSTAS --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

		# dicionario de apostas APOSTA[nome_jogador] = (quanto_aposta, qual_aposta)
		APOSTAS = dict()	

		# loop de apostas por jogador
		for nome in FICHAS.keys():

			# loop de verificação de qual é a aposta
			while True:

				# input de qual aposta
				qual_aposta = input('Qual a sua aposta? (banco/jogador/empate)')

				# verifica validade da entrada
				if qual_aposta not in ['Banco', 'Jogador', 'Empate']:
					print('Não entendi.')
					continue

				# caso nada de errado ocorra, sai do loop
				break
			
			# loop de verificação do quanto é a aposta
			while True:

				# input do valor da aposta
				quanto_aposta = input('%s, quanto você quer apostar?' % nome)

				# verifica se é um número
				try: quanto_aposta = int(quanto_aposta)
				except:
					print('Não entendi.')
					continue

				# verifica suficiência de fundos
				if quanto_aposta > FICHAS[nome]:
					print('Você não tem tudo isso.')
					continue

				# gracinha
				if quanto_aposta == 0: print('Bunda mole.')

				# caso nada de errado ocorra, sai do loop
				break
			
			# registra a aposta
			APOSTAS[nome]= (qual_aposta, quanto_aposta)
			
		# --- --- PASSO 2: EMBARALHAR --- --- --- --- --- --- --- --- --- --- --- --- --- ---

		# define o bolo de jogo a partir do baralho de referência
		bolo = list(BARALHO)

		# embaralha o bolo
		embaralhar(bolo)







