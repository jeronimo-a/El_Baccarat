'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
15/10/2020

Módulo que contém as falas do jogo
'''

falas = dict()

falas['numero baralhos'] = {
	'pergunta': 'Com quantos baralhos gostaria de jogar? (1, 6 ou 8) ',
	'fora da whitelist': 'Não jogamos com essa quantidade de baralhos.',
	'tipo errado': 'Isso não é nem sequer um número.',
	'tipo errado 2': 'Uma das possibilidades, por favor.'
}

falas['numero jogadores'] = {
	'pergunta': 'Quantas pessoas vão apostar? ',
	'tipo errado': 'Preciso de um número.',
	'tipo errado 2': 'Crianças não apostam. Um número inteiro, por favor.'
}

falas['nomes'] = {
	'pergunta': 'Qual o nome do jogador ;? ',
	'dentro da blacklist': 'Eu tenho que chamá-lo de algo.'
}

falas['qual aposta'] = {
	'pergunta': 'Qual a sua aposta, ;? (E, B, ou J) ',
	'fora da whitelist': 'Não entendi. Pode ser empate (E), banco (B) ou jogador (J).'
}

falas['quanto aposta'] = {
	'pergunta': 'Quanto você quer apostar? ',
	'maior que o maximo': 'Você não tem tudo isso.',
	'menor que o minimo': 'Impossível.',
	'tipo errado': 'Preciso de um número.',
	'tipo errado 2': 'Apenas valores inteiros.'
}

falas['bandeiras'] = {
	'inicio jogo': 'Bem-vindo(s)!',
	'inicio rodada': 'Vamos começar as apostas!'
}

falas['tirar sarro'] = {
	'sem aposta': 'frangote.'
}