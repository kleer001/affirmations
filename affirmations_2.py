#
# afirmations v2 improvements
# started Tue May 10 10:32:03 PDT 2016
# by: Clear Menser
# 

import os
import random
import time
import logging
import datetime

from twilio.rest import TwilioRestClient 

#set current directory to own location? 
os.chdir(os.path.dirname(full_path))

#pick a random numbr of second, var for log
waiting = random.randint(1,3600)

#sleep that much
time.sleep(waiting)

#find the time for log
currentTime = 'Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())


#### - Start up the affirmation building - #######

# first get the file and start building the affirmation
line = random.choice(open('affirmations.txt').readlines())

repeat = random.randint(2,5)

variations = [
' with your eyes closed and your heart open.',
' with your eyes unfocused and your mind open.',
' with your eyes unfocused and your heart open.',
' with your eyes closed and your mind open.',
' your eyes closed and your heart open.',
' your eyes unfocused and your mind open.',
' your eyes unfocused and your heart open.',
' your eyes closed and your mind open.',
]

suffix = ' - Is your daily affirmation. Please slowly repeat it '+str(repeat)+' times to yourself,'
suffix += variations[random.randint(3,5)]

line = line + suffix

# put your own SECRET credentials here 
ACCOUNT_SID = open('ACCOUNT_SID.dat').read()
AUTH_TOKEN = open('AUTH_TOKEN.dat').read() 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

#my twilio Number, Menny in Yellow Knife
myTwilioNumber = '+18679882273'
#Wendy's number, moved to file
toCellPhoneNumber = "GET FROM FILE"
#my number : 
#toCellPhoneNumber = '+16047248711'

client.messages.create( 
	body=line,
	from_=myTwilioNumber,
	to=toCellPhoneNumber   
)

#create log
logging.basicConfig(filename='affirmations.log',level=logging.DEBUG)

#everything all at once
logging.info('%s  %s seconds waited - %s',currentTime ,waiting, line)


