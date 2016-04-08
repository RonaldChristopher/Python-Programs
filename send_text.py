from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account = "AC3b730c9fc6be1ff27e792d42f7f50bbd"
auth_token  = "a378aafef3590a6eff987bf03b2ffac3"
client = TwilioRestClient(account, auth_token)
 
message = client.messages.create(
    to="+13472792132",    # Replace with your phone number
    from_="+13474640195",  # Replace with your Twilio number
    body="Hi.. :) Ron here, just wrote a code..and it worked... I love you <3") 


