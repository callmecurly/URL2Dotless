import os												# Importing OS Library from python3
import socket 											# Importing socket Library from python3
import requests											# Importing requests Library from python3

def banner():											# Defining a function called banner
	print( """\n 
							   __  __     _____   ____        __  __              
							  / / / /____/ /__ \ / __ \____  / /_/ /__  __________
							 / / / / ___/ /__/ // / / / __ \/ __/ / _ \/ ___/ ___/
							/ /_/ / /  / // __// /_/ / /_/ / /_/ /  __(__  |__  ) 
							\____/_/  /_//____/_____/\____/\__/_/\___/____/____/            
													
								#  Coded with love by :- @10zyc | @saycureIO
							   # InfoSec | https://saycure.io/L0zyc | # StaySayCure
		 """)											# Printing ascii art with personal info
		 
		 
def validate():											# Defining a function called validate 
	UAgent={'User-Agent': 'Mozilla/5.0 (Macintosh); Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}				# Providing a fake user-agent
	try:												# 
		validate= requests.head("http://" + url, headers=UAgent) # validating if the URL responds with status code 200 on http										
		if validate.status_code != 200:					# If the status code with http is not 200
			validate= requests.head("https://" + url, headers=UAgent) # Validating if the URL responds with status code 200 on https
		if validate.status_code == 200:					# If status code is 200
			dlessConv()									# Calling function dlessConv

	except requests.ConnectionError:					# When the output encounters an error
		print("Host not found")							# "Host not found" Message is displayed


def dlessConv():										# Defining a function called dlessConv
	hname=socket.gethostbyname(url)						# Getting the IP Address from the host
	spl=hname.split(".")								# Splitting the IP Address into string
	sep=[int(e) for e in spl]							# Looping the values of spl into sep as integer 
	a,b,c,d=sep											# Listing the values of sep into a, b, c and d 
	dotless=256*(256*(a*256+b)+c)+d						# Converting into dotless ip
	print("\nYour requested dotless IP is: http://%s" %dotless)	# Printing the Dotless IP value of given URL


banner()												# Calling function banner

url= input(" Enter url: ")										# Taking URL input from the user

if "https://" in url:									# Checking if the URL contains "https://"
	url= url.replace("https://", "")					# Replacing "https://" with nothing on the URL
	dlessConv()											# Calling function dlessConv after replacing the url

elif "http://" in url:									# Checking if the URL contains "https://"
	url= url.replace("http://", "")						# Replacing "http://" with nothing on the URL
	dlessConv()											# Calling function dlessConv after replacing the url

elif "127.0.0.1" in url:								# Checking if the URL parameter contains "127.0.0.1"
	print (" \nThe dotless ip for localhost is: http://2130706433") #Printing the dotless IP value of given URL

elif "localhost" in url:								#Checking if the URL parameter contains "localhost"
	print (" \nThe dotless ip for localhost is: http://2130706433") #Printing the dotless IP value of given URL
	
else:													# If the URL does not contain any of the above parameters
	validate()											# Calling the function validate