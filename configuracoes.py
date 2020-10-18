'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
18/10/2020

Módulo que contém as configurações do jogo
'''

TAXAS = {
	'E': 8,
	'J': 1,
	'B': 0.95
}

COMISSAO = {
	1: {'E': 0.1575, 'B': 0.0101, 'J': 0.0129},
	6: {'E': 0.1444, 'B': 0.0106, 'J': 0.0124},
	8: {'E': 0.1436, 'B': 0.0106, 'J': 0.0124}
}

POSSIBILIDADES_DE_BARALHOS = [1, 6, 8]