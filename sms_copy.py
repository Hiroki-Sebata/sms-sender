from twilio.rest import Client

account_sid = 'account_sid from twoilio goes here'
auth_token = 'authentication token from twoilio goes here'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+your twoilio phone number goes here',
  body='hello',
  to='to your phone number'
)

print(message.sid)