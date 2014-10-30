import unittest
import expr_aritmetica

class TestsExprAritmetica(unittest.TestCase):

	def test_extraer_operandos_y_operadores_en_2_mas_2(self):
		expresion = expr_aritmetica.ExprArtimetica()
		self.failUnless({'Operandos' : [2,2], 'Operadores' : ['+']},
			expresion.parse("2 + 2"))

	def test_extraer_operadores_en_10_entre_menos_5(self):
		expresion = expr_aritmetica.ExprArtimetica()
		self.failUnlessEqual({'Operandos': [10, -5], 'Operadores': ['/']}, expresion.parse("10 / -5"))