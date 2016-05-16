#
# afirmations tests
# started Sat May  7 12:33:37 PDT 2016
# finished? Sat May  7 17:00:11 PDT 2016
# nope... Tue May 10 10:19:13 PDT 2016 AHahaha
# by: Clear Menser
# 

import os
import random
import time
import logging
import datetime

from twilio.rest import TwilioRestClient 

#current directory, because that's where everything is 
#probably a waaaaay better way to do this, own location? 
os.chdir('/Users/3crows/Dropbox/ai/code/affirmations/')

#pick a random numbr of second, var for log
waiting = random.randint(1,3600)

#sleep that much
time.sleep(waiting)

#find the time for log
currentTime = 'Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())

# first get the file and start building the affirmation
line = random.choice(open('affirmations.txt').readlines())

# then capitalize the first letter
# and that's quite silly, I will go in a fix data soon
# add reminder text at the end
line = '\"'+line[0].upper()+line[1:]+'\"' 

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

suffix = ' is your daily affirmation. Please slowly repeat it '+str(repeat)+' times to yourself,'
suffix += variations[random.randint(0,7)]

line = line + suffix

# put your own SECRET credentials here 
ACCOUNT_SID = "AC4544810e68e4b71ebce61640912b79a5" 
AUTH_TOKEN = "1fcb10dc9f73bd6b0be48203fba65eea" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

#my twilio Number, Menny in Yellow Knife
myTwilioNumber = '+18679882273'
#Wendy's number, moved to file
toCellPhoneNumber = '+16047738089'
#my number : 
#toCellPhoneNumber = '+16047248711'

client.messages.create( 
	body=line,
	from_=myTwilioNumber,
	to=toCellPhoneNumber   
)


logging.basicConfig(filename='affirmations.log',level=logging.DEBUG)


logging.info('%s  %s seconds waited',currentTime ,waiting)
logging.info('%s', line)


