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

	# criação do baralho imutável (referência somente)
	BARALHO = construir_baralhos(1)	# por enquanto só 1

	#definir numero de jogadores
	while True:
		jogadores= input("quantos jogadores?")
		try: 
			jogadores= int(jogadores)
			break
		except:
			print("Número de jogadores inváilido" )
			continue 

	
	#Nomeação dos jogadores e atribuição de fichas 
	JOGADORES= dict()
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

