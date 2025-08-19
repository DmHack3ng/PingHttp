import requests
from bs4 import BeautifulSoup
import re

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-s", "--website", dest="web",
                  help="[+] Put your Website")


(options, args) = parser.parse_args()


def banner():
	art = r"""
.-----------------------------------.
| _   _ _   _   ____  _             |
|| | | | |_| |_|  _ \(_)_ __   __ _ |
|| |_| | __| __| |_) | | '_ \ / _` ||
||  _  | |_| |_|  __/| | | | | (_| ||
||_| |_|\__|\__|_|   |_|_| |_|\__, ||
|                             |___/ |
'-----------------------------------'
		"""

	print(art)

banner()

s=requests.get("https://crt.sh/?q="+options.web).text


z=options.web

one=z.split(".")[0]
two=z.split(".")[1]




t=BeautifulSoup(s,"html.parser")

allA=t.find_all("td")


lnk_List=[]

for a in allA:
	#d=re.search(r'(?i)\b(?:[a-z0-9-]+\.)*serveu\.fr\b',a.text)
	d=re.search(r'(?i)\b(?:[a-z0-9-]+\.)*'+one+"\\."+two,a.text)
	if d:
		domain= d.group(0).strip()
		#print(domain)
		if domain not in lnk_List and "www" not in a.text:
			#print(domain)
			lnk_List.append(domain)
			try:
				req= requests.get("https://"+domain)
				if req.status_code == 200 or 301 or 403:
					print("[+] Found Valid URL "+"https://"+domain+":"+str(req.status_code))
			except:
				pass
