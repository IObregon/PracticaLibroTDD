import expr_aritmetica
import calculadora

class Supercalculadora:
	def __init__(self, parser):
		self.calc = calculadora.Calculadora()
		self.parser = parser

	def __operar__(self, expr_decompuesta):
		i = None
		res_intermedio = 0
		if '/' in expr_decompuesta['Operadores']:
			i = expr_decompuesta['Operadores'].index('/')
			res_intermedio = self.calc.dividir(
				expr_decompuesta['Operandos'][i],
				expr_decompuesta['Operandos'][i + 1])
		elif '-' in expr_decompuesta['Operadores']:
			i = expr_decompuesta['Operadores'].index('-')
			res_intermedio = self.calc.restar(
				expr_decompuesta['Operandos'][i],
				expr_decompuesta['Operandos'][i + 1])
		elif '+' in expr_decompuesta['Operadores']:
			i = expr_decompuesta['Operadores'].index('+')
			res_intermedio = self.calc.sumar(
				expr_decompuesta['Operandos'][i],
				expr_decompuesta['Operandos'][i + 1])
		else:
			assert False

		return (i, res_intermedio)


	def __simplificar__(self, expr_decompuesta):
		if expr_decompuesta['Operadores'] == []:
			return expr_decompuesta

		(i, res_intermedio) = self.__operar__(expr_decompuesta)
		expr_simplificada = expr_decompuesta
		expr_simplificada['Operadores'].pop(i)
		expr_simplificada['Operandos'].pop(i)
		expr_simplificada['Operandos'].pop(i)
		expr_simplificada['Operandos'].insert(i, res_intermedio)

		return self.__simplificar__(expr_simplificada)

	def calcular(self, expresion):
		return str(self.__simplificar__(self.parser.parse(expresion))['Operandos'][0])