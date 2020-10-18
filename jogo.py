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
	numero_jogadores = solicitar_entrada(falas['numero jogadores'], 'int')

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
		FICHAS[nome] = 1000

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

		# --- --- PASSO 4, 5, 6 e 7: VERIFICA GANHADORES E DISTRIBUI CARTAS RECORRENTEMENTE --- --- --- --- --- --- --- --- --- --- --- ---

		# calcula as somas da mão do jogador e do banco
		SOMA_JOGADOR = soma_cartas(MAO_JOGADOR)
		SOMA_BANCO = soma_cartas(MAO_BANCO)

		print()
		mostrar_maos(MAO_JOGADOR, MAO_BANCO, SOMA_JOGADOR, SOMA_BANCO)

		# variáveis booleanas, determinam se algum dos dois finalizou, ou seja, somou 8 ou 9
		jogador_finalizou = SOMA_JOGADOR in [8,9]
		banco_finalizou = SOMA_BANCO in [8,9]

		# bandeiras da condicao de distribuicao da terceira carta
		sem_finalizadores = not (jogador_finalizou or banco_finalizou)	# True para ninguém com soma 8 ou 9
		alguem_recebendo = not SOMA_JOGADOR in [6,7] or not SOMA_BANCO in [6,7]	# False para ambos com soma 6 ou 7

		# condicao de distribuicao da terceira carta
		if sem_finalizadores and alguem_recebendo:


			# dá a carta extra ao jogador, caso não tenha somado 6 ou 7
			if SOMA_JOGADOR not in [6,7]:

				# retira uma carta do bolo e a adiciona à mão do jogador
				MAO_JOGADOR.append(BOLO.pop())
				SOMA_JOGADOR = soma_cartas(MAO_JOGADOR)

				mostrar_maos(MAO_JOGADOR, MAO_BANCO, SOMA_JOGADOR, SOMA_BANCO)

				# variável booleana, determina se o jogador somou 8 ou 9
				jogador_finalizou = SOMA_JOGADOR in [8,9]


			# dá a carta extra ao banco, caso não tenha somado 6 ou 7, e o jogador não tenha finalizado
			if SOMA_BANCO not in [6,7] and not jogador_finalizou:

				# retira uma carta do bolo e a adiciona à mão do banco
				MAO_BANCO.append(BOLO.pop())
				SOMA_BANCO = soma_cartas(MAO_BANCO)

				mostrar_maos(MAO_JOGADOR, MAO_BANCO, SOMA_JOGADOR, SOMA_BANCO)

				# variável booleana, determina se o banco somou 8 ou 9 
				banco_finalizou = SOMA_BANCO in [8,9]

		# atualiza as bandeiras da condição conforme os novos valores
		sem_finalizadores = not (jogador_finalizou or banco_finalizou)
		alguem_recebendo = not SOMA_JOGADOR in [6,7] or not SOMA_BANCO in [6,7]

		# se ambos ficaram presos em 6 ou 7, ou se ambos somaram 8 ou 9
		if not alguem_recebendo or (jogador_finalizou and banco_finalizou):

			# verifica quem tem a soma maior
			if SOMA_JOGADOR == SOMA_BANCO: RESULTADO = 'E'
			elif SOMA_JOGADOR > SOMA_BANCO: RESULTADO = 'J'
			elif SOMA_BANCO > SOMA_JOGADOR: RESULTADO = 'B'

		# se somente um dos dois finalizou
		elif not sem_finalizadores:

			# verifica quem finalizou
			if jogador_finalizou: RESULTADO = 'J'
			elif banco_finalizou: RESULTADO = 'B'

		# --- --- --- PAGAMENTO DAS APOSTAS --- --- --- --- --- --- ---

		# loop de pagamento, vai de aposta em aposta
		for nome in APOSTAS.keys():

			# variáveis usadas com frequência
			qual_aposta = APOSTAS[nome][0]
			quanto_aposta = APOSTAS[nome][1]

			# se errou a aposta
			if not qual_aposta == RESULTADO:

				# caso acabou de perder tudo, imprimir fala apropriada
				if FICHAS[nome] == quanto_aposta: print(nome + falas['pagamento']['perdeu tudo'])

				# caso contrário
				else: print(nome + falas['pagamento']['perdeu'], str(quanto_aposta), end=' fichas.\n')

				# subtrai a perda do total de fichas
				FICHAS[nome] -= quanto_aposta

				# quebra o loop
				continue

			# calcula o ganho, levando em conta a comissão do cassino
			ganho = int(TAXAS[qual_aposta] * quanto_aposta * (1 - COMISSAO[numero_baralhos][qual_aposta]))

			# verifica se ganhou com empate, nesse caso, imprime fala apropriada
			if RESULTADO == 'E': print(nome + falas['pagamento']['ganhou E'], str(ganho), end=' fichas, com a nossa comissão já inclusa.\n')

			# caso contrário
			else: print(nome + falas['pagamento']['ganhou'], str(ganho), end=' fichas, considerando a nossa comissão.\n')

			# adiciona o ganho às fichas
			FICHAS[nome] += ganho











