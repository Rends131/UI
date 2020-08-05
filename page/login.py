#!/usr/bin/env python
#author:wuya

from selenium import  webdriver
from selenium.webdriver.common.by import By
from base.base import WebUi,AppUi
from appium import webdriver
import time as t
from base.base import Base


class LoginPage(AppUi):

	loginRegisterButton = (By.ID,'cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin')
	passwordLoginButton = (By.ID,'cn.xiaochuankeji.tieba:id/login_mode')
	username_loc = (By.ID,'cn.xiaochuankeji.tieba:id/phone_num_edit')
	password_loc = (By.ID,'cn.xiaochuankeji.tieba:id/code_edit')
	login_loc = (By.ID,'cn.xiaochuankeji.tieba:id/login')
	meButton_loc = (By.ID,'cn.xiaochuankeji.tieba:id/me_item')


	@property
	def meButtonClick(self):
		"""点击我的"""
		print('等5秒，点击我的')
		t.sleep(5)
		return self.findElement(*self.meButton_loc).click()


	@property
	def loginRegister(self):
		"""点击登录"""
		print('等5秒，点击登录')
		t.sleep(5)
		return self.findElement(*self.loginRegisterButton).click()

	@property
	def passwordLogin(self):
		"""点击账号密码登录"""
		print('等5秒，点击账号密码登录')
		t.sleep(5)
		return self.findElement(*self.passwordLoginButton).click()

	def username(self,name):
		"""输入账号"""
		self.findElement(*self.username_loc).send_keys(name)

	def password(self,password):
		"""输入密码"""
		self.findElement(*self.password_loc).send_keys(password)

	@property
	def clickLogin(self):
		"""点击登录"""
		self.findElement(*self.login_loc).click()

	def login(self,name,passwd):
		self.meButtonClick
		self.loginRegister
		self.passwordLogin
		self.username(name)
		self.password(passwd)
		self.clickLogin
		t.sleep(5)


class LoginPageWeb(WebUi):
	username_loc=(By.ID,'freename')
	password_loc=(By.ID,'freepassword')
	login_loc=(By.LINK_TEXT,'登录')
	div=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]')
	nick=(By.XPATH,'//*[@id="user_id"]/em[2]')
	exit_loc=(By.XPATH,'//*[@id="warpMain"]/div[4]/div[1]/div[3]/div[3]/span/a')

	def username(self,name):
		self.findElement(*self.username_loc).send_keys(name)

	def password(self,password):
		self.findElement(*self.password_loc).send_keys(password)

	@property
	def clickLogin(self):
		self.findElement(*self.login_loc).click()

	@property
	def getDiv(self):
		t.sleep(1)
		return self.findElement(*self.div).text

	def login(self,name,passwd):
		self.username(name)
		self.password(passwd)
		self.clickLogin
		t.sleep(5)

	@property
	def getNick(self):
		t.sleep(1)
		return self.findElement(*self.nick).text

	@property
	def exit(self):
		self.findElement(*self.exit_loc).click()
		t.sleep(3)




