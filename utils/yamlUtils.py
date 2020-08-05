#!/usr/bin/env python
#author:wuya

from common.read_file import filePath
import  yaml

class YamlUtils:

	@staticmethod
	def readYaml():
		with open(filePath(),'r',encoding='utf-8') as f:
			return list(yaml.safe_load_all(f))

	@staticmethod
	def getVlue(index=0,key='web',value='url'):
		return YamlUtils.readYaml()[index][key][value]

if __name__ == '__main__':
    print(YamlUtils.getVlue(2,'login','username'))