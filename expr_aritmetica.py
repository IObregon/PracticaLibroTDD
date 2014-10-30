import string

class ExprArtimetica:
	def parse(self, exp):
		operandos = []
		operadores = []
		tokens = string.split(exp)
		for token in tokens:
			try:
				operandos.append(string.atoi(token))
			except ValueError:
				operadores.append(token)
		return {'Operandos' : operandos, 'Operadores' : operadores}