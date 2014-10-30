import supercalculadora
import calculadora
import expr_aritmetica
import unittest

class TestSupercalculadora (unittest.TestCase):
	def setUp(self):
		self.sc = supercalculadora.Supercalculadora(
			expr_aritmetica.ExprAritmetica())

	def tearDown(self):
		pass
	def test_sumar(self):
		self.failUnlessEqual("4", self.sc.calcular("2 + 2"))

	def test_restar(self):
		self.failUnlessEqual("0", self.sc.calcular("2 - 2"))

	def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
		self.failUnlessEqual("6", self.sc.calcular("5 + 4 - 3"))

	def test_expresion_compleja_sin_parentesis_con_precedencia(self):
		self.failUnlessEqual("3", self.sc.calcular("5 + 4 / 2 - 4"))
		self.failUnlessEqual("-1", self.sc.calcular("4 / 2 - 3"))
		self.failUnlessEqual("1", self.sc.calcular("4 / 2 - 3 + 1 + 6 / 3 - 1"))
		self.failUnlessEqual("-8", 
			self.sc.calcular("4 / -2 + 3 + -1 + -6 / -3 - 10"))