#!/usr/bin/env python
#author:wuya

import  os

def path():
	return os.path.dirname(os.path.dirname(__file__))

def filePath(director='config',fileName='config.yaml'):
	return os.path.join(path(), director, fileName)




