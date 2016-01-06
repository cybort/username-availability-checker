#Takes username as Input
#Needs the following dependencies :
# pip install requests[security]
# pip install termcolor

import requests
from termcolor import colored

username = raw_input("Enter the username : ")
sites = ["facebook", "twitter", "instagram", "github", "soundcloud"]

def check(status_code):
	if(status_code == 404):
		print colored('Available', 'green')
	else: 
		print colored('Taken', 'red')

for i, val in enumerate(sites):
	a = requests.head("https://"+sites[i]+".com/"+username)
	print "https://"+sites[i]+".com/"+username
	check(a.status_code)




