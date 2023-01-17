import os
from twilio.rest import Client

def send(msg):   
    account_sid = 'ACf7b3ac69de595ac62985e5a02ec93552' 
    auth_token = 'a9a143548b21300d0a2c8107d9b538e0'
    client = Client(account_sid, auth_token)
 
    message = client.messages.create(
            body = msg,
            from_='+14793398570',
            to='+18482563099'
        )

