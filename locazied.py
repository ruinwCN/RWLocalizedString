#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 遍历某目录下所有文件

import os
import os.path
import re

dirpath = r"/Users/Yu/Work/test"

global mySet;
mySet = set();

def writeToFile():
	'''
	写文件
	'''
	global mySet
	ansList=list(mySet)
	for d in ansList:
		print d;
		fmx = open("Localizable.strings", "a")
		myd = '\n' + '\"' + str(d) + '\" = \"' + str(d) + '\";';
		fmx.write(myd);
		fmx.close();


def addToSet(string):
	global mySet;
	mySet.add(string);


def getInternationalizationString(string):
	'''
	获取国际化字符串
	'''
	mylist = re.findall(r"NSLocalizedString\(@\"(.+?)\",",string);
	if len(mylist) != 0:
		for index in mylist:
			#print ( 'find :',index );
			addToSet(mylist[0]);

	# if "NSLocalizedString" in string:
	# 	print (string);
	return string;

#获取当前目录
# now_dirpath = os.getcwd();
# print ('nowDirPath is '+ now_dirpath);
#print (os.listdir(now_dirpath));

#clear
fc = open("Localizable.strings", "wb");
fc.truncate();
fc.close();

for root,dirs,files in os.walk(dirpath):
	# for d in dirs:
	# 	print os.path.join(root, d)
	for f in files:	

		if os.path.splitext(f)[1] == '.m':
			print os.path.join(root, f);
			#打开文件
			file = open(os.path.join(root, f), "r");
			#读每一行
			for linenum, line in enumerate(file.readlines()):
				#print (getInternationalizationString(line));
				getInternationalizationString(line);

writeToFile();

print ('end...');

#file_ergodic(now_dirpath);

