from twilio.rest import Client import os
# Your Account SID from twilio.com/console
account_sid = "AC0fd8259feac0af2db824199c6a49d7f0"
# Your Auth Token from twilio.com/console
auth_token = "67d734b3ed35c92b18bf12024e7fc128"
client = Client (account_sid, auth_token)
message client.messages.create(
to="+12345995159", from_="+12345995159", body="Hello from Python!")
print (message.sid)%
