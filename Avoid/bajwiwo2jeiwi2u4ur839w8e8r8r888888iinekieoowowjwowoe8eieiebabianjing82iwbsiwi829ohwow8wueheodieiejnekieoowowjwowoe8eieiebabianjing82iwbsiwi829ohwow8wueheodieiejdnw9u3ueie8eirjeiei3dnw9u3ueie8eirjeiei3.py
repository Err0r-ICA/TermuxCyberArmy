# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

#hay manusia udah nyampe di sini ea  ubah author ataupun ngerecode semoga emak bapaknya mati dalam keadaan mengenaskan
#buat yg nyampe di sini cuman buat mempelajari pemrograman dan beberapa fungsinya ane ucapin selamat berjuang
#tapi awaslu yg nge recode ataupun mengganti author

def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)

def wa():
    os.system('xdg-open https://www.instagram.com/termux_hacking/?hl=it')

def ressture():
   os.system('clear')
   print '\x1b[1;33m╔╦══════════════════════════════════╗\n║║ Already Have an ID And Password? ║\n╚╣╔═════════════════════════════════╝\n╔╝╚═════════════════════╗'
   print '\x1b[1;33m║\033[48;5;0;38;5;197mLOGIN TO CONTINUE      ║\n╠═══════════════════════╝\033[48;5;0;38;5;202m'
   user = raw_input('║ID      : \033[48;5;0;38;5;209m')
   import getpass
   sandi = raw_input('║PW      : ')
   if sandi == 'ItaliaCyberArmy' and user == 'ERR0R':
      print '║LOGIN SUCCSESS\n╚═══════\x1b[1;91m▶'
      sys.exit
   else:
      print 'Login FAILED, Please Contact ADMIN'
      time.sleep(1)
      wa()
      ressture()

def loding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCheck \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)
        

ressture()
os.system('bash hsowkaksisisiaiowowkwkaiske.sh')
