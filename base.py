'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém as funções base do jogo
'''

def construir_baralhos(quantidade):
	'''	constrói "x" baralhos completos de cartas sem naipe
		retorna uma lista de números que representam as cartas

		1: ás, 2: dois, 11: J, 12: Q, 13: K '''

	# objeto de retorno
	baralho = list()

	# cria quatro grupos de cartas (um para cada naipe):
	for nipe in range(1,5):
		
		# loop de criação das cartas individuais
		for numero in range(1, 14):
			carta= (nipe, numero)
			baralho.append(carta)

	# retorna o objeto imutável multiplicado
	return tuple(baralho * quantidade)


def soma_cartas(cartas):
	''' recebe uma lista de cartas e retorna o valor da
		soma a partir das regras do Bacará

		ás: 1, dois: 2, ..., dez: 0, J: 0, Q: 0, K: 0 '''

	# base da soma
	soma = 0

	# loop de soma
	for carta in cartas:

		# ignora as cartas acima de nove
		if carta > 9: continue

		# soma o valor das demais cartas
		soma += carta[1]
	

	# descarte das dezenas
	soma %= 10

	# retorna a soma
	return soma


print(construir_baralhos(1))
