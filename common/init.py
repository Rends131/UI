#!/usr/bin/env python
#author:wuya


import  unittest
from selenium import  webdriver
from utils.yamlUtils import YamlUtils

class Init(unittest.TestCase):
	def setUp(self) -> None:
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get(YamlUtils.getVlue())
		self.driver.implicitly_wait(30)

	def tearDown(self) -> None:
		self.driver.quit()