'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém as funções base do jogo
'''

def baralhos(quantidade):
	'''	constrói "x" baralhos completos de; retorna uma
		tupla de tuplas que representam as cartas
		
		carta: (naipe, número)
		
		naipes - 1: ouros, 2: espadas, 3: copas, 4: paus
		números - 1: ás, 2: dois, 11: J, 12: Q, 13: K '''

	# objeto de retorno
	baralho = list()

	# cria quatro grupos de cartas (um para cada naipe):
	for naipe in range(1,5):
		
		# loop de criação das cartas individuais
		for numero in range(1, 14):
			carta = (naipe, numero)
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
		if carta[1] > 9: continue

		# soma o valor das demais cartas
		soma += carta[1]
	

	# descarte das dezenas
	soma %= 10

	# retorna a soma
	return soma


def solicitar_entrada(saidas, tipo_esperado, whitelist=[], blacklist=[], variavel_pergunta=None, marcador_variavel=None, minimo=None, maximo=None):
	''' pede entradas do(s) jogador(es) e verifica a validade da entrada
		levando em conta tipo de dado esperado e valores esperados

		retorna a resposta processada '''

	# clona o dicionario afim de não alterá-lo fora do escopo da função
	saidas = dict(saidas)
	
	# verifica se a pergunta contém uma variável, caso sim, a insere na pergunta
	if variavel_pergunta != None:

		# define a lista dos caracteres da pergunta
		lista_char = list(saidas['pergunta'])

		# define a posicao do marcador de posição da variável
		indice_variavel = lista_char.index(marcador_variavel)

		# substitui o marcador pela variável e redefine a variável original
		lista_char[indice_variavel] = variavel_pergunta
		saidas['pergunta'] = str().join(lista_char)

	# loop de verificação
	while True:
		
		# solicita a entrada
		resposta = input(saidas['pergunta'])

		# caso o tipo esperado for um número inteiro
		if tipo_esperado == 'int':

			# verifica se a entrada é um número
			try: resposta = float(resposta)

			# caso não for, reinicia o loop
			except:
				print(saidas['tipo errado'])
				continue

			# verifica se o número é inteiro, se não for, reinicia o loop
			if resposta != int(resposta):
				print(saidas['tipo errado 2'])
				continue

			# verifica se o número tem que estar dentro de um intervalo
			if minimo != None and maximo != None:

				# se maior que o máximo, reinicia o loop
				if resposta > maximo:
					print(saidas['maior que o maximo'])
					continue

				# se menor que o mínimo, reinicia o loop
				if resposta < minimo:
					print(saidas['menor que o minimo'])
					continue

			# transforma a entrada em um int, finalmente
			resposta = int(resposta)

		# verifica se a resposta está entre as esperadas
		if resposta not in whitelist and len(whitelist) > 0:
			print(saidas['fora da whitelist'])
			continue

		# verifica se a resposta está entre as bloqueadas
		if resposta in blacklist:
			print(saidas['dentro da blacklist'])
			continue

		# quebra o loop de verificação
		break

	# retorna a resposta processada
	return resposta





