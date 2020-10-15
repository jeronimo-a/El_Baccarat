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
	BARALHO = construir_baralhos(numero_baralhos)	# por enquanto só 1

	# pergunta o número de jogadores
	while True:
		jogadores= input("quantos jogadores?")
		try: 
			jogadores= int(jogadores)
			break
		except:
			print("Número de jogadores inváilido" )
			continue 

	
	#Nomeação dos jogadores e atribuição de fichas 
	JOGADORES = dict()
	for i in range(jogadores):
		nome= input("Qual o nome do jogador %d ?" % i)
		JOGADORES[nome]=1000




	# bandeira de rodada, caso False a rodada termina
	RODADA = True

	# loop de rodada, quando acaba a rodada finaliza
	while RODADA:
		APOSTAS= dict()	
		for nome in JOGADORES.keys():
			
		# --- --- PASSO 1 --- --- --- --- --- --- --- --- ---
			while True:

				aposta_qte= input("Quanto quer apostar?")
				try:
					aposta_qte=int(aposta_qte)
					if aposta_qte > JOGADORES[nome]:
						print("aposta maior do que o número de fichas")

						continue
					break
				except:

					print("Não entendi")
					continue	
					
			while True:
				aposta_quem= input("Apostar na Banco ou no Jogador?")
				if aposta_quem not in ["Banco", "Jogador", "Empate"]:
					print("Não entendi")
					continue
				break

			APOSTAS[nome]= (aposta_qte, aposta_quem)
			








		# *** definir apostas aqui ***

		# --- --- PASSO 2 --- --- --- --- --- --- --- --- ---
		# define o bolo de jogo a partir do baralho de
		# referência e embaralha as cartas
		bolo = list(BARALHO)
		embaralhar(bolo)

