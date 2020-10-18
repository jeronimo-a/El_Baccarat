'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém o loop principal de jogo
'''

from base import *	# importa todas as funções base
from falas import falas	# importa as falas do jogo
from random import shuffle as embaralhar	# importa a função de embaralhamento

# bandeira de programa, caso False, o programa finaliza
PROGRAMA = True

# loop principal do programa, quando acaba, o programa finaliza
while PROGRAMA:

	# bandeira de jogo, caso False, o jogo termina
	JOGO = True

	# loop principal de jogo, quando acaba, o jogo em questão finaliza
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

			# --- --- PASSO 1: APOSTAS --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

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
				

			# --- --- PASSO 2: EMBARALHAR --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

			# define o bolo de jogo a partir do baralho de referência
			BOLO = list(BARALHO)

			# embaralha o bolo
			embaralhar(BOLO)

			# --- --- PASSO 3: DISTRIBUIR --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

			MAO_JOGADOR = []
			MAO_BANCO = []

			MAO_JOGADOR.append(BOLO.pop())
			MAO_BANCO.append(BOLO.pop())
			MAO_JOGADOR.append(BOLO.pop())
			MAO_BANCO.append(BOLO.pop())

			# --- --- PASSO 4, 5, 6 e 7: VERIFICA GANHADORES E DISTRIBUI CARTAS RECORRENTEMENTE --- --- --- --- --- --- --- --- --- --- --- ---

			soma_jogador = soma_cartas(MAO_JOGADOR)
			soma_banco = soma_cartas(MAO_BANCO)

			print('MÃO DO JOGADOR:', str(MAO_JOGADOR))
			print('SOMA JOGADOR: %d' % soma_jogador)

			print('MÃO DO BANCO:', str(MAO_BANCO))
			print('SOMA BANCO: %d' % soma_banco)

			jogador_ganhou = soma_jogador in [8, 9]
			banco_ganhou = soma_banco in [8, 9]

			sem_ganhador = not (jogador_ganhou or banco_ganhou)

			jogador_finalizado = soma_jogador in [6, 7]
			banco_finalizado = soma_banco in [6, 7]

			todos_finalizados = jogador_finalizado and banco_finalizado


			# loop de distribuição das cartas extras
			while sem_ganhador and not todos_finalizados:

				jogador_recebe = (banco_finalizado or len(MAO_JOGADOR) == len(MAO_BANCO)) and not jogador_finalizado
				banco_recebe = len(MAO_JOGADOR) > len(MAO_BANCO) and not banco_finalizado

				if jogador_recebe:

					MAO_JOGADOR.append(BOLO.pop())
					soma_jogador = soma_cartas(MAO_JOGADOR)

					print('MÃO DO JOGADOR:', str(MAO_JOGADOR))
					print('SOMA JOGADOR: %d' % soma_jogador)

					jogador_ganhou = soma_jogador in [8, 9]
					jogador_finalizado = soma_jogador in [6, 7]


				if banco_recebe:

					MAO_BANCO.append(BOLO.pop())
					soma_banco = soma_cartas(MAO_BANCO)

					print('MÃO DO BANCO:', str(MAO_BANCO))
					print('SOMA BANCO: %d' % soma_banco)

					banco_ganhou = soma_banco in [8, 9]
					banco_finalizado = soma_banco in [6, 7]

				sem_ganhador = not (jogador_ganhou or banco_ganhou)
				todos_finalizados = jogador_finalizado and banco_finalizado


			if todos_finalizados:

				if soma_jogador == soma_banco: RESULTADO = 'E'
				elif soma_jogador > soma_banco: RESULTADO = 'J'
				elif soma_banco > soma_jogador: RESULTADO = 'B'

			if not sem_ganhador:

				if jogador_ganhou and banco_ganhou:

					if soma_jogador == soma_banco: RESULTADO = 'E'
					elif soma_jogador > soma_banco: RESULTADO = 'J'
					elif soma_banco > soma_jogador: RESULTADO = 'B'

				elif jogador_ganhou: RESULTADO = 'J'
				elif banco_ganhou: RESULTADO = 'B'

			print(RESULTADO)










