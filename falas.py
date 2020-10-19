'''
EP - Design de Software
Jerônimo Afrange e Lucas Quadros
16/10/2020

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
	'pergunta': 'Quantas pessoas vão apostar? No máximo ;. ',
	'tipo errado': 'Preciso de um número.',
	'maior que o maximo': 'Jogadores demais.',
	'menor que o minimo': 'Impossível.',
	'tipo errado 2': 'Crianças não apostam. Um número inteiro, por favor.'
}

falas['nomes'] = {
	'pergunta': 'Qual o nome do jogador ;? ',
	'dentro da blacklist': 'Esse nome não vale.'
}

falas['qual aposta'] = {
	'pergunta': 'Qual a sua aposta, ;? (E, B, ou J) ',
	'fora da whitelist': 'Não entendi. Pode ser empate (E), banco (B) ou jogador (J).'
}

falas['quanto aposta'] = {
	'pergunta': 'Quanto você quer apostar? Você tem ; fichas. ',
	'maior que o maximo': 'Você não tem tudo isso.',
	'menor que o minimo': 'Impossível.',
	'tipo errado': 'Preciso de um número.',
	'tipo errado 2': 'Apenas valores inteiros.'
}

falas['bandeiras'] = {
	'inicio jogo': '\nBem-vindo(s)!\n',
	'inicio rodada': '\nVamos começar as apostas!',
	'adeus': '\nTchau, tchau! Obrigado por jogar.\n',
	'jogar novamente': '\nMuito bem, então. Vamos jogar!\n',
	'ganhador': 'O ganhador da rodada foi o ',
	'empate': 'A rodada empatou!'
}

falas['tirar sarro'] = {
	'sem aposta': 'frangote.'
}

falas['pagamento'] = {
	'perdeu': 'Você perdeu',
	'perdeu tudo': 'Você perdeu tudo, não pode mais jogar.',
	'ganhou E': 'Que sorte! Você ganhou',
	'ganhou': 'Você ganhou',
	'info': ', você apostou no '
}

falas['fim de jogo'] = {
	'pergunta': '\nNinguém tem fichas sobrando. Gostaria(m) de jogar de jogar novamente? (S/N) ',
	'fora da whitelist': 'Não entendi. Responda apenas com "S" ou "N", por favor.'
}






