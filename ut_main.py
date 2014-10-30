import unittest
import ut_calculadora
import ut_expr_aritmetica
import ut_supercalculadora

if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(ut_calculadora.TestCalculadora))
	suite.addTest(unittest.makeSuite(ut_expr_aritmetica.TestsExprAritmetica))
	suite.addTest(unittest.makeSuite(ut_supercalculadora.TestSupercalculadora))
	unittest.TextTestRunner(verbosity=3).run(suite)
	

	






