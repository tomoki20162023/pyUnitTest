import unittest
from datetime import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome import service

from myTestCase import MyTestCase

class Test4Selenium(MyTestCase):
	CHROME_DRIVER_PATH = "C:/Tools/selenium/chromedriver_win32/98_0_4758_102/chromedriver.exe"
	#CHROME_DRIVER_PATH = "/mnt/c/Tools/selenium/chromedriver_win32/98_0_4758_102/chromedriver.exe"

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		options = webdriver.ChromeOptions()
		options.add_argument('--disable-gpu')
		options.add_argument('--disable-dev-shm-usage')
		cls.service = service.Service(executable_path=cls.CHROME_DRIVER_PATH)
		cls.driver = webdriver.Chrome(service=cls.service, options=options)

	def setUp(self):
		super().setUp()

	def test_upper(self):
		val:str = 'Foo'
		self.assertEqual('foo'.upper(), 'FOO')
		with self.subTest(msg='subTest sample', val=val):
			# self.assertEqual(val, 'FOO')
			self.assertNotEqual(val, 'FOO')

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)
		self.skipTest("skip test")

	def test_open(self):
		# self.driver.get("https://www.google.com/")
		self.driver.get("file:///E:/programs/html/LanguagesInfo/html/index.html")
		time.sleep(3)
		res = self.driver.execute_script("""
			return $('#refC').text();
		""")
		print(res)

	def test_screenshot(self):
		self.driver.get("file:///E:/programs/html/LanguagesInfo/html/index.html")

		dtf = "%Y%m%d-%H%M%S-%f"
		today = datetime.today()
		#ssPath = "E:/programs/python/pyUnitTestPS/test-screen-shot-" + today.strftime(dtf) + ".png"
		ssPath = "screenshot/test-screen-shot-" + today.strftime(dtf) + ".png"
		self.driver.get_screenshot_as_file(ssPath)
		self.driver.execute_script("$('#refC').text('python unittest sample');")

		today = datetime.today()
		#ssPath = "E:/programs/python/pyUnitTestPS/test-screen-shot-" + today.strftime(dtf) + ".png"
		ssPath = "screenshot/test-screen-shot-" + today.strftime(dtf) + ".png"
		self.driver.get_screenshot_as_file(ssPath)

	def tearDown(self):
		super().tearDown()

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		super().tearDownClass()

def suite():
	suite = unittest.TestSuite()
	for testcase in [tc for tc in dir(Test4Selenium) if tc.startswith("test_")]:
		suite.addTest(Test4Selenium(testcase))
	return suite

def strTupples(tupples):
		ss = "["
		ss += ("" if len(tupples) == 0 else "\n\t" + "\n\t".join(map(str, tupples)) + "\n")
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
		print("\t" + "\n\t".join(filter(lambda d: d.startswith("test_"), dir(Test4Selenium))))
		for testcase in [tc for tc in dir(Test4Selenium) if tc.startswith("test_")]:
			print("testcase : " + testcase)

