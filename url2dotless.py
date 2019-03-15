#!/usr/bin/python3																		# The script can run through bash
import os																				# Importing OS Library from python3
import socket 																			# Importing socket Library from python3
import requests																			# Importing requests Library from python3

def banner():																			# Defining a function called banner
	print( """\n 																		
							   __  __     _____   ____        __  __              
							  / / / /____/ /__ \ / __ \____  / /_/ /__  __________
							 / / / / ___/ /__/ // / / / __ \/ __/ / _ \/ ___/ ___/
							/ /_/ / /  / // __// /_/ / /_/ / /_/ /  __(__  |__  ) 
							\____/_/  /_//____/_____/\____/\__/_/\___/____/____/ v0.4a          
													
								#  Coded with love by :- @L0zyc | @saycureIO
							   # InfoSec | https://saycure.io/L0zyc | # StaySayCure
		 """)																			# Printing ascii art with personal info		

httpHeaders={																			# Providing a fake user-agent
			'User-Agent': 'Mozilla/5.0 (Macintosh); Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.8',
			'Accept-Encoding': 'gzip'
			}																			

def validate(url):																		# Defining a function called validate 
	if "http" in url or "https" in url:													# If the URL input contains http or https
		req=requests.head(url, headers=httpHeaders)										# Validate if the host responds
		if req.status_code == 200:														# If host replies with response code 200
			strip(url)																	# Sending URL to strip function
		else:																			# Executes when response code is not 200 from the host
			if "http" in url or "https" in url:											# If the URL contains http or https
				strip(url)																# Sending URL to strip function
	elif "127.0.0.1" in url or "localhost" in url:										# If the URL input contains 127.0.0.1 or localhost keywords 
		print (" \nThe dotless ip for localhost is: http://2130706433")					# Print the dotless ip for 127.0.0.1 or localhost
	else:																				# When none of the above condition match
		try:																			# Trying with
			req=requests.head("https://" + url, headers=httpHeaders)					# Adding https:// to URL and validating response 
			if req.status_code != 200:													# If the response of the host is not 200
				req=requests.head("http://" + url, headers=httpHeaders)					# Trying with http://
			if req.status_code == 200:													# If the host responds with code 200 
				dlessConv(url)															# Sending the url for dotless conversion
			else:																		# If none of the conditions meet
				print("Try host with www.%s" % url)										# Suggesting the user to try adding www. to the url
		except requests.ConnectionError:												# If all the above conditions fail		
			print("Host not found")														# Message is displayed
				
def strip(url):																			# Defining a function called strip
	url= url.replace("http://", "")														# Replacing "http://" with nothing on the URL
	url= url.replace("https://", "")													# Replacing "https://" with nothing on the URL
	validate(url)																		# Sending the output to function validate

def dlessConv(url):																		# Defining a function called dlessConv
	hname=socket.gethostbyname(url)														# Getting the IP Address from the host
	spl=hname.split(".")																# Splitting the IP Address into string
	sep=[int(e) for e in spl]															# Looping the values of spl into sep as integer 
	a,b,c,d=sep																			# Listing the values of sep into a, b, c and d 
	dotless=256*(256*(a*256+b)+c)+d														# Converting into dotless ip
	print("\nYour requested dotless IP is: http://%s\n" %dotless)						# Printing the Dotless IP value of given URL
	
banner()																				# Calling banner function
url = validate(input("Enter: "))														# Taking input from the host 