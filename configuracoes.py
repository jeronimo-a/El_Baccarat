'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
18/10/2020

Módulo que contém as configurações do jogo
'''

FICHAS_INICIAIS = 1000

MAXIMO_JOGADORES = 10

TAXAS = {
	'E': 8,
	'J': 1,
	'B': 0.95
}

POSSIBILIDADES_DE_APOSTA = {
	'E': 'empate',
	'J': 'jogador',
	'B': 'banco'
}

COMISSAO = {
	1: {'E': 0.1575, 'B': 0.0101, 'J': 0.0129},
	6: {'E': 0.1444, 'B': 0.0106, 'J': 0.0124},
	8: {'E': 0.1436, 'B': 0.0106, 'J': 0.0124}
}

POSSIBILIDADES_DE_BARALHOS = [1, 6, 8]

REGRAS_TERCEIRA_CARTA = [
	[1,1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,0,1],
	[0,0,1,1,1,1,1,1,0,0],
	[0,0,0,0,1,1,1,1,0,0]
]



