import unittest
from myTestCase import MyTestCase

class Test5StringMethods(MyTestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()

	def setUp(self):
		super().setUp()

	def test_1(self):
		self.assertEqual(1, 1)

	def test_2(self):
		self.assertEqual(2, 2)

	def test_3(self):
		self.skipTest("skipped.")

	def test_4(self):
		self.assertEqual(4, 5)

	def tearDown(self):
		super().tearDown()

	@classmethod
	def tearDownClass(cls):
		super().tearDownClass()

def suite():
	suite = unittest.TestSuite()
	for m in filter(lambda d: d.startswith("test_"), dir(Test5StringMethods)):
		suite.addTest(Test5StringMethods(m))
	return suite

def strTupples(tupples):
		ss = "["
		ss += ("" if len(tupples) == 0 else "\n\t" + "\n\t".join(map(lambda t: str(t[0]) + "\n" + t[1], tupples)) + "\n")
		ss += "]"
		return ss

if __name__ == '__main__':
	from pprint import pprint

	print("test starts.")
	testProgram:unittest.TestProgram = None
	try:
		MyTestCase.setEnv("chrome driver")
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
		for m in filter(lambda d: d.startswith("test_"), dir(Test5StringMethods)):
			print(m)

