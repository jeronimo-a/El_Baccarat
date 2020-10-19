'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém o loop principal de jogo
'''

from base import *	# importa todas as funções base
from falas import falas	# importa as falas do jogo
from random import shuffle as embaralhar	# importa a função de embaralhamento
from configuracoes import * 	# importa as configurações de jogo

# bandeira de programa, caso False, o programa finaliza
PROGRAMA = True

# fala de início de jogo
if PROGRAMA: print(falas['bandeiras']['inicio jogo'])

# loop principal do programa, quando acaba, o programa finaliza
while PROGRAMA:

	# pergunta com quantos baralhos jogar, verificando erros
	numero_baralhos = solicitar_entrada(
		falas['numero baralhos'],
		'int', whitelist=POSSIBILIDADES_DE_BARALHOS
		)

	# criação do baralho imutável (referência somente)
	BARALHO = baralhos(numero_baralhos)

	# pergunta quantas pessoas vão jogar, verificando erros
	numero_jogadores = solicitar_entrada(
		falas['numero jogadores'],
		'int', minimo=1,
		maximo=MAXIMO_JOGADORES,
		variavel_pergunta=str(MAXIMO_JOGADORES),
		marcador_variavel=';'
		)

	# nomeação dos jogadores e atribuição de fichas 
	FICHAS = dict()	# FICHAS[nome_jogador] = fundos_jogador

	blacklist = ['']

	# pergunta o nome dos jogadores
	for n in range(1, numero_jogadores + 1):

		# solicita o nome dos jogadores, verificando erros
		nome = solicitar_entrada(
			falas['nomes'], 'str',
			blacklist=blacklist,
			variavel_pergunta=str(n),
			marcador_variavel=';'
			)

		blacklist.append(nome)

		# define quantidade de fichas do jogador
		FICHAS[nome] = FICHAS_INICIAIS

	# bandeira de rodada, caso False a rodada termina
	JOGO = True

	# --- --- --- --- --- loop de rodada, quando acaba a rodada finaliza --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
	while JOGO:

		# verifica se alguém ainda tem dinheiro
		if max(FICHAS.values()) == 0:

			resposta = solicitar_entrada(falas['fim de jogo'], 'str', whitelist=['S', 'N'])
			JOGO = False

			PROGRAMA = resposta == 'S'

			if not PROGRAMA: print(falas['bandeiras']['adeus'])
			else: print(falas['bandeiras']['jogar novamente'])
			
			break

		# variável do resultado
		RESULTADO = None

		# fala de início de rodada
		print(falas['bandeiras']['inicio rodada'])

		# --- --- PASSO 1: APOSTAS --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

		# dicionario de apostas
		APOSTAS = dict()	# APOSTA[nome_jogador] = (quanto_aposta, qual_aposta)

		# loop de apostas por jogador
		for nome in FICHAS.keys():

			# não pergunta para jogadores sem dinheiro
			if FICHAS[nome] == 0: continue

			print()	# print de espaçamento

			# pergunta qual é a aposta, verificando erros
			qual_aposta = solicitar_entrada(
				falas['qual aposta'], 'str',
				whitelist=POSSIBILIDADES_DE_APOSTA.keys(),
				variavel_pergunta=nome,
				marcador_variavel=';'
				)

			# pergunta quanto quer apostar, verificando erros
			quanto_aposta = solicitar_entrada(
				falas['quanto aposta'], 'int',
				variavel_pergunta=str(FICHAS[nome]),
				marcador_variavel=';',
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

		# --- --- PASSO 4, 5, 6 e 7: VERIFICA GANHADORES E DISTRIBUI AS TERCEIRAS CARTAS --- --- --- --- --- --- --- --- --- --- --- ---

		# calcula as somas da mão do jogador e do banco
		SOMA_JOGADOR = soma_cartas(MAO_JOGADOR)
		SOMA_BANCO = soma_cartas(MAO_BANCO)

		print('\n\nRESULTADOS:')

		# mostra as cartas tiradas
		mostrar_maos(MAO_JOGADOR, MAO_BANCO, SOMA_JOGADOR, SOMA_BANCO)

		# no caso de nenhum dos dois somar 8 ou 9
		if not (SOMA_JOGADOR in [8,9] or SOMA_BANCO in [8,9]):

			# se o jogador somar menos de 6, dar terceira carta
			if SOMA_JOGADOR < 6:
				terceira_carta = BOLO.pop()
				MAO_JOGADOR.append(terceira_carta)
				SOMA_JOGADOR = soma_cartas(MAO_JOGADOR)

				mostrar_maos(MAO_JOGADOR, MAO_BANCO, SOMA_JOGADOR, SOMA_BANCO)

			# determina se o banco recebe a terceira carta
			if SOMA_BANCO < 6 and SOMA_JOGADOR not in [8,9]:

				# se o jogador não tiver retirado a terceira carta, o banco retira
				if SOMA_JOGADOR in [6,7]:

					MAO_BANCO.append(BOLO.pop())
					SOMA_BANCO = soma_cartas(MAO_BANCO)

				# ainda determina se o banco recebe a terceira carta, a partir da regra avançada
				elif REGRAS_TERCEIRA_CARTA[SOMA_BANCO][terceira_carta[1] % 10] == 1:

					MAO_BANCO.append(BOLO.pop())
					SOMA_BANCO = soma_cartas(MAO_BANCO)

				mostrar_maos(MAO_JOGADOR, MAO_BANCO, SOMA_JOGADOR, SOMA_BANCO)


		# verifica quem tem a maior soma e imprime o vencedor
		if SOMA_BANCO == SOMA_JOGADOR:
			RESULTADO = 'E'
			print(falas['bandeiras']['empate'].upper(), end='\n\n')

		elif SOMA_BANCO > SOMA_JOGADOR: RESULTADO = 'B'
		elif SOMA_BANCO < SOMA_JOGADOR: RESULTADO = 'J'

		if RESULTADO != 'E':
			print(falas['bandeiras']['ganhador'].upper() + POSSIBILIDADES_DE_APOSTA[RESULTADO].upper() + '.', end='\n\n')

		# --- --- --- PAGAMENTO DAS APOSTAS --- --- --- --- --- --- ---

		# loop de pagamento, vai de aposta em aposta
		for nome in APOSTAS.keys():

			print()	# print de espaçamento

			# variáveis usadas com frequência
			qual_aposta = APOSTAS[nome][0]
			quanto_aposta = APOSTAS[nome][1]

			print(nome + ', você apostou ' + str(quanto_aposta) + ' no ' + POSSIBILIDADES_DE_APOSTA[qual_aposta] + '.')

			# se errou a aposta
			if not qual_aposta == RESULTADO:

				# caso acabou de perder tudo, imprimir fala apropriada
				if FICHAS[nome] == quanto_aposta: print(falas['pagamento']['perdeu tudo'], end='\n')

				# caso contrário
				else: print(falas['pagamento']['perdeu'], str(quanto_aposta), end=' fichas.\n')

				# subtrai a perda do total de fichas
				FICHAS[nome] -= quanto_aposta

				# quebra o loop
				continue

			# calcula o ganho, levando em conta a comissão do cassino
			ganho = int(TAXAS[qual_aposta] * quanto_aposta * (1 - COMISSAO[numero_baralhos][qual_aposta]))

			# verifica se ganhou com empate, nesse caso, imprime fala apropriada
			if RESULTADO == 'E': print(falas['pagamento']['ganhou E'], str(ganho), end=' fichas, com a nossa comissão já inclusa.\n')

			# caso contrário
			else: print(falas['pagamento']['ganhou'], str(ganho), end=' fichas, considerando a nossa comissão.\n')

			# adiciona o ganho às fichas
			FICHAS[nome] += ganho











