import unittest
from unittest import mock

class MyTestCase(unittest.TestCase):
	__driver = ""

	@classmethod
	def setUpClass(cls):
		pcls = cls.__mro__[1]
		pcls.NAME = cls.__mro__[1].__name__
		pcls.testcode = mock.Mock()
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@classmethod
	def tearDownClass(cls):
		pcls = cls.__mro__[1]
		MyTestCase.showDriverName()
		pcls.testcode()
		pass

	@staticmethod
	def showDriverName():
		print(MyTestCase.__driver)

	@staticmethod
	def setEnv(browser_driver):
		MyTestCase.__driver = browser_driver

