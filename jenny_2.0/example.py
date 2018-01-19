import logging
from twilio.rest import Client

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('Script start')
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC47591910f555d88fb94243901fc9d3b0"
auth_token = "c9d3b24654e4e749a9ca9003fe75adae"
client = Client(account_sid, auth_token)

message = client.messages.create(
        "+13397075117",
        body="Test",
        from_="+12566395742")

print(message.sid)
logging.debug('Script end')