qtd_casos = int(input())

assassinatos = {}
vitimas = []
detetives = []

for caso in range(qtd_casos):
	assassino, vitima, detetive = input().split()

	if assassino not in assassinatos:
		assassinatos[assassino] = []
	assassinatos[assassino].append(vitima)

	vitimas.append(vitima)
	detetives.append(detetive)

pessoas = set(list(assassinatos) + vitimas + detetives)
dados_pessoas = {}

for pessoa in pessoas:
	dados_pessoas[pessoa] = {}
	dados_pessoas[pessoa]['assassinados'] = {'assassino': 0, 'vitima': 0, 'detetive': 0}

	vitimas_pessoa = assassinatos.get(pessoa, [])
	for vitima in vitimas_pessoa:
		if vitima in detetives:
			dados_pessoas[pessoa]['assassinados']['detetive'] += 1
		elif vitima in assassinatos:
			dados_pessoas[pessoa]['assassinados']['assassino'] += 1
		else:
			dados_pessoas[pessoa]['assassinados']['vitima'] += 1

	dados_pessoas[pessoa]['vitima'] = vitimas.count(pessoa)
	dados_pessoas[pessoa]['detetive'] = detetives.count(pessoa)

print('-' * 60)
for pessoa in sorted(pessoas):
	complemento = ''
	if dados_pessoas[pessoa]['vitima'] > 0:
		complemento = ' (in memoriam)'
		titulo = 'vítima inocente'

	matou = ''
	if sum(dados_pessoas[pessoa]['assassinados'].values()) > 0:
		titulo = 'assassino(a)'
		for tipo_vitima in ('detetive', 'assassino', 'vitima'):
			qtd_mortes = dados_pessoas[pessoa]['assassinados'][tipo_vitima]
			if qtd_mortes > 0:
				matou += '  Matou {} {}(s).\n'.format(qtd_mortes, tipo_vitima)
		matou = matou.replace('vitima', 'inocente')

	resolveu = ''
	qtd_casos = dados_pessoas[pessoa]['detetive']
	if qtd_casos > 0:
		titulo = 'detetive'
		resolveu = '  Resolveu {} caso(s).\n'.format(qtd_casos)

	apresentacao = '{}{}: {}.\n'.format(pessoa, complemento, titulo)

	relatorio = apresentacao + resolveu + matou
	print(relatorio + '-' * 60)