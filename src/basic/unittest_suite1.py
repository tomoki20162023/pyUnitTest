import unittest
from myTestCase import MyTestCase

import test01
from test02 import test02
from test03 import test03
#import test04
import test05

def suite():
	print("set test suite")
	suite = unittest.TestSuite()
	suite.addTest(test01.Test1StringMethods('test_upper'))
	suite.addTest(test02.Test2StringMethods('test_isupper'))
	suite.addTests(test03.suite())
	suite.addTests(test05.suite())
	print("set done")
	return suite

if __name__ == '__main__':
	print("start test suite")
	MyTestCase.setEnv("test driver")
	runner = unittest.TextTestRunner()
	runner.run(suite())
	print("end test suite")
