import unittest
from myTestCase import MyTestCase

class Test1StringMethods(MyTestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()

	def setUp(self):
		super().setUp()

	def test_upper(self):
		val:str = 'Foo'
		self.assertEqual('foo'.upper(), 'FOO')
		with self.subTest(msg='subTest sample', val=val):
			# self.assertEqual(val, 'FOO')
			self.assertNotEqual(val, 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)
		self.skipTest("skip test")

	def tearDown(self):
		super().tearDown()

	@classmethod
	def tearDownClass(cls):
		super().tearDownClass()

def strTupples(tupples):
		ss = "["
		ss += ("" if len(tupples) == 0 else "\n" + "\n".join(map(lambda x: "  " + x, map(str, tupples))) + "\n")
		ss += "]"
		return ss

if __name__ == '__main__':
	from pprint import pprint

	print("test starts.")
	testProgram:unittest.TestProgram = None
	try:
		testProgram = unittest.main(exit=False)
		result = testProgram.result
		print("tests   : " + str(result.testsRun))
		print("failures: " + strTupples(result.failures))
		print("errors  : " + strTupples(result.errors))
		print("skipped : " + strTupples(result.skipped))

	except Exception as e:
		pprint(e)
	finally:
		print("test done.")

