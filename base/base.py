#!/usr/bin/env python
#author:wuya

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium import  webdriver
from utils.logUtils import LogUtils
import time

class Base(object):


	def initDriver(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '7.1.2'
		desired_caps['noReset'] = 'True'
		desired_caps['deviceName'] = 'Android Emulator'
		desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
		desired_caps['appActivity'] = '.ui.base.SplashActivity'
		desired_caps['unicodeKeyboard'] = 'True'
		desired_caps['resetKeyboard'] = 'True'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		time.sleep(10)
		return self.driver


class Factory:
	def __init__(self,driver):
		self.driver=driver

	def createFactory(self,driver):
		if driver=='web':
			return WebUi()
		elif driver=='app':
			return AppUi()
		else:pass

class WebDriver:
	def __init__(self,driver):
		self.driver=driver

	def __str__(self):
		return 'driver'

	def findElement(self,*loc):
		try:
			return WebDriverWait(
				driver=self.driver,
				timeout=10).until(lambda x: x.find_element(*loc))
		except NoSuchElementException as e:
			return e.args[0]

	def findElements(self,*loc):
		try:
			return WebDriverWait(
				driver=self.driver,
				timeout=10).until(lambda x: x.find_elements(*loc))
		except NoSuchElementException as e:
			raise e.args[0]


class WebUi(WebDriver):
	def __str__(self):
		return 'web'

class AppUi(WebDriver):
	def __str__(self):
		return 'app'

