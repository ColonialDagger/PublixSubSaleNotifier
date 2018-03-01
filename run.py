import time
import requests
import config
import sys
from bs4 import BeautifulSoup
from twilio.rest import Client

def pullrequest(): # Defines pullrequest() to pull source from url
	print("\n\n\nPulling new web page at %s...") % (time.time())
	pull = requests.get("http://arepublixchickentendersubsonsale.com/") # Pulls source code from web page
	soup = BeautifulSoup(pull.content,"html.parser") # Cleans source code
	print('New web page pulled succesfully!')
	return soup # Returns formatted source code

def eval():
	soup = str(pullrequest())
	if 'onsale:yes' in soup: # When goes on sale
		return True
	elif 'onsale:yes' not in soup: # When goes off sale
		return False

def andr_notify(prompt): # Defines andr_notify() to notify via SMS with Twilio API
	print("Logging into Twilio...")
	auth_token = "7af1a7d84d073c21de011c9522ae3018"
	client = Client(config.account_sid,config.auth_token)
	print("Sending messages...")
	for x in config.numbers:
		client.api.account.messages.create(
			to=x, # Outbound recievers
			from_="+17865395514", # Outbound sender
			body=prompt) # Outbound message
	print("Messages sent at %s!") % (time.time())

def sleep(sleep_time):
	for i in range(sleep_time+1):
		print("Sleeping for " + str(sleep_time - i) + " more seconds...")
		sys.stdout.write("\033[F") # Cursor up one line
		time.sleep(1)

prev_sale = "null"
while True: # Run forever
	onsale = eval()
	if onsale != prev_sale: # Checks for change in
		change = True
	
	if onsale and change: # If sale has started
		prev_sale = True # Adds variable for state of previous cycle to be true
		change = False # Resets change
		print(config.promptstart)
		andr_notify(config.promptstart) # Sends SMS
	elif not onsale and change: # If sale has ended
		prev_sale = False # Adds variable for state of previous cycle to be false
		change = False # Resets change
		print(config.promptend)
		andr_notify(config.promptend) # Sends SMS
	
	sleep(config.sleep_time) # Sleeps before beginning new cycle