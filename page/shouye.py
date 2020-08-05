#!/user/bin/env python
#coding=utf-8

from selenium import  webdriver
from selenium.webdriver.common.by import By
from base.base import WebUi,AppUi
import time as t

class ShouyePage(AppUi):
	shouyeButttonloc = (By.ID,'cn.xiaochuankeji.tieba:id/home_item')
	naviButtonloc = (By.ID,'cn.xiaochuankeji.tieba:id/title')
	forumListContentloc = (By.ID,'cn.xiaochuankeji.tieba:id/expand_content_view')
	forumDetailTitleloc = (By.ID,'cn.xiaochuankeji.tieba:id/tvTitle')
	pinglunInputloc = (By.ID,'cn.xiaochuankeji.tieba:id/etInput')
	sendButtonloc = (By.ID,'cn.xiaochuankeji.tieba:id/send')
	sendContentloc = (By.ID,'cn.xiaochuankeji.tieba:id/expandTextView')

	@property
	def shouyeButttonClick(self):
		"""点击首页按钮"""
		t.sleep(1)
		return self.findElement(*self.shouyeButttonloc).click()

	@property
	def getNaviContent(self):
		t.sleep(1)
		return self.findElement(*self.naviButtonloc)

	@property
	def forumListContentClick(self):
		t.sleep(1)
		return self.findElement(*self.forumListContentloc).click()

	@property
	def forumDetailTitle(self):
		t.sleep(2)
		return self.findElement(*self.forumDetailTitleloc).text

	def pinglunInput(self,inputData):
		t.sleep(2)
		return self.findElement(*self.sendButtonloc).send_keys(inputData)

	@property
	def sendButtonClick(self):
		self.findElement(*self.sendButtonloc).click()

	@property
	def sendContent(self):
		t.sleep(8)
		return self.findElement(*self.sendContentloc)