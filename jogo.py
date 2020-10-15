'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém o loop principal de jogo
'''

# --- CONSTRÓI UM BARALHO COMUM DE 54 CARTAS QUE NÃO SERÁ ALTERADO --- --- ---

# carta: (naipe, número)
BARALHO = list()

# cria as cartas naipe por naipe:
# (1: ouros, 2: espadas, 3: copas, 4: paus)
for naipe in range(1,5):
	
	# loop de numeração das cartas
	# (1: ás, 2: dois, 11: valete, 12: dama)
	for numero in range(1, 14):

		# (3, 1): ás de copas
		carta = (naipe, numero)
		BARALHO.append(carta)

BARALHO = tuple(BARALHO)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
