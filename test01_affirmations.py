# afirmations tests
# started Sat May  7 12:33:37 PDT 2016
# by: Clear Menser
#



from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC4544810e68e4b71ebce61640912b79a5" 
AUTH_TOKEN = "1fcb10dc9f73bd6b0be48203fba65eea" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

#my twilio Number, Menny in Yellow Knife
myTwilioNumber = '+18679882273'
#Wendy's number
toCellPhoneNumber = '+16047738089'
#my number : 
#toCellPhoneNumber = '+16047248711'


client.messages.create( 
	body='Testing SMS from program from Clear :D',
	from_=myTwilioNumber,
	to=toCellPhoneNumber   
)

