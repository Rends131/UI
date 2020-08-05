#!/usr/bin/env python
#author:wuya

import logging
from common.read_file import filePath

class LogUtils:
	@staticmethod
	def log():
		logger = logging.getLogger(__file__)
		logger.setLevel(logging.DEBUG)
		# 定义格式
		fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s')

		# 控制台的输出
		fh_stream = logging.StreamHandler()
		fh_stream.setLevel(logging.DEBUG)
		fh_stream.setFormatter(fmt=fmt)

		# 写到文件里面
		fh_file = logging.FileHandler(filePath('log','console.log'), 'a', encoding='utf-8')
		fh_file.setLevel(logging.DEBUG)
		fh_file.setFormatter(fmt=fmt)

		# 添加到handler里面
		logger.addHandler(fh_stream)
		logger.addHandler(fh_file)
		return logger

