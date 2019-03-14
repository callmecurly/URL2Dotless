### importing Libraries ###

import os									#Importing OS Library from python3
import socket 								#Importing socket Library from python3
import requests								#Importing requests Library from python3

def dlessConv():
	hname=socket.gethostbyname(url)				#Getting the IP Address from the host
	spl=hname.split(".")						#Splitting the IP Address 
	sep=[int(e) for e in spl]
	a,b,c,d=sep
	dotless=256*(256*(a*256+b)+c)+d
	print("Your requested dotless IP is: http://%s" %dotless)
	
url = input ("URL: ")

# Validating the URL provided by the user

headers={'User-Agent': 'Mozilla/5.0 (Macintosh); Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

try:
	validate= requests.head("http://" + url, headers=headers)

	if validate.status_code != 200:
		validate= requests.head("https://" + url, headers=headers)
	
	if validate.status_code == 200:
		dlessConv()
		
except requests.ConnectionError:
    print("Host not found")