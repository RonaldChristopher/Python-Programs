from twilio import rest

account = "AC3b730c9fc6be1ff27e792d42f7f50bbd"
token = "a378aafef3590a6eff987bf03b2ffac3"
client = rest.TwilioRestClient(account, token)

message = client.messages.create(to="+1xxxxxxxxxx", from_="+13474640195",
                                 body="Hello there!")
