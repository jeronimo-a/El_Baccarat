'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém o loop principal de jogo
'''

# --- CONSTRÓI UM BARALHO COMUM DE 52 CARTAS QUE NÃO SERÁ ALTERADO --- --- ---

# carta: número
# não há necessidade de especificar o naipe
BARALHO = list()

# cria quatro grupos de cartas:
for _ in range(4):
	
	# loop de numeração das cartas
	# 1: ás, 2: dois, 11: J, 12: Q, 13: K
	for carta in range(1, 14):
		BARALHO.append(carta)

BARALHO = tuple(BARALHO)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
