#!/user/bin/env python
#coding=utf-8

import unittest
from page.shouye import ShouyePage
from page.login import LoginPage
from base.base import Base
from utils.yamlUtils import YamlUtils

class TestShouYe(unittest.TestCase):

	def setUp(self):
		print('开始出事话')
		self.driver=Base().initDriver()
		print('初始化完成')

	def testshouye01_01(self):
		"""验证首页导航栏文案显示是否正常"""
		LoginPage(self.driver).login(name=YamlUtils().getVlue(2,'login','username'),passwd=YamlUtils().getVlue(2,'login','passwd'))
		m = ShouyePage(self.driver)
		m.shouyeButttonClick
		self.assertEqual(m.getNaviContent[0].text,YamlUtils().getVlue(1,'naviText','huati'))

	# def testshouye01_02(self):
	# 	"""验证帖子列表内容"""
	# 	m = ShouyePage(self.driver)
	# 	m.forumListContentClick
	# 	self.assertEqual(m.forumDetailTitle,YamlUtils().getVlue(3,'forumDetail','title'))
	#
	# def testshouye01_03(self):
	# 	"""验证评论帖子功能"""
	# 	m = ShouyePage(self.driver)
	# 	m.forumListContentClick
	# 	m.pinglunInput("testxuehai")
	# 	m.sendButtonClick
	# 	sendContent=m.sendContent
	# 	sendContentRawList=[]
	# 	for i in range(0,len(sendContent)):
	# 		sendContentRawList.append(sendContent[i].text)
	# 	sendContentList="".join(sendContentRawList)
	# 	self.assertIn("textxuehai",sendContentList)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)