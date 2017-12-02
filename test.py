
from slackclient import SlackClient

token = "TOKEN"
sc = SlackClient(token)
chan="CANAL"
greeting="FRASEs"
print sc.api_call("chat.postMessage", as_user="true:", channel=chan, text=greet$
