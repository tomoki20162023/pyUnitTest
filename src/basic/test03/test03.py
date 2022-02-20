import unittest
from myTestCase import MyTestCase

class Test3StringMethods(MyTestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(Test3StringMethods('test_isupper'))
	return suite

if __name__ == '__main__':
#	runner = unittest.TextTestRunner()
#	runner.run(suite())
	unittest.main()

