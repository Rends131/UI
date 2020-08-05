#!/usr/bin/env python
#author:wuya



import  unittest
import os
import  HTMLTestRunner
import  time
from utils.logUtils import LogUtils
from common.read_file import filePath


def getSuites():
	'''获取所有的测试点'''
	suites=unittest.defaultTestLoader.discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_*.py',
		top_level_dir=None
	)
	return suites


def getNowTime():
	return time.strftime('%y-%m-%d-%H-%M-%S',time.localtime())


def run():
	filename=filePath('report',getNowTime()+'report.html')
	runner=HTMLTestRunner.HTMLTestRunner(
		stream=open(filename,'wb'),
		verbosity=2,
		title='自动化测试报告',
		description='自动化测试详细的报告'
	).run(getSuites())
	LogUtils.log().info('测试结束，生成基于HTML的测试报告')

if __name__ == '__main__':
    run()


