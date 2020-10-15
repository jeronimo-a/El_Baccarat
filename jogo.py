'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém o loop principal de jogo
'''

# --- CONSTRÓI UM BARALHO COMUM DE 52 CARTAS PARA REFERÊNCIA --- --- ---

# carta: número
# não há necessidade de especificar o naipe
BARALHO = list()

# cria quatro grupos de cartas:
for _ in range(4):
	
	# loop de numeração das cartas
	# 1: ás, 2: dois, 11: J, 12: Q, 13: K
	for carta in range(1, 14):
		BARALHO.append(carta)

# torna o objeto inalterável
BARALHO = tuple(BARALHO)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# --- FUNÇÕES ÚTEIS --- --- --- --- --- --- --- --- --- --- --- --- ---

def soma_cartas(cartas):
	''' recebe uma lista de cartas e retorna o valor
		da soma a partir das regras do Bacará '''

	# base da soma
	soma = 0

	# loop de soma
	for carta in cartas:

		# ignora as cartas acima de nove
		if carta > 9: continue

		# soma o valor das demais cartas
		soma += carta

	# descarte das dezenas
	soma %= 10

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

