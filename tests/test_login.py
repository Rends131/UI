#!/usr/bin/env python
#author:wuya

import  unittest
from page.login import LoginPageWeb
from selenium import webdriver
import  time as t
from common.init import Init
from  utils.logUtils import LogUtils
from utils.yamlUtils import YamlUtils

class TestShouYe(Init,LoginPageWeb):
	def test_sina_login_null(self):
		'''sina验证:用户名和密码为空'''
		self.login('','')
		self.assertEqual(self.getDiv,YamlUtils().getVlue(1,'sina','loginNull'))

	def test_sina_email(self):
		'''sina验证:邮箱格式不正确'''
		self.login('asewr','srty')
		self.assertEqual(self.getDiv,YamlUtils().getVlue(1,'sina','email'))

	def test_sina_div(self):
		'''sina验证:错误的用户名和密码'''
		self.login('wewrt@sina.com','aerwtr')
		self.assertEqual(self.getDiv,YamlUtils().getVlue(1,'sina','error'))

	def test_sina_login_success(self):
		'''sina验证:登录成功'''
		self.login(name=YamlUtils().getVlue(2,'login','username'),passwd=YamlUtils().getVlue(2,'login','passwd'))
		self.assertEqual(self.getNick,YamlUtils().getVlue(2,'login','username'))

	def test_sina_exit_success(self):
		'''sina验证:退出成功'''
		self.login(name=YamlUtils().getVlue(2,'login','username'),passwd=YamlUtils().getVlue(2,'login','passwd'))
		self.exit
		self.assertTrue(str(self.driver.current_url).endswith('logout'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
