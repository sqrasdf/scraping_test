import http.client, urllib
from datetime import datetime

api_token = "as7kmkwzoaxu7bzwdz6rjycp25rm2a"  # app token
user_key = "u759ikjxp3m64f91oudv2gd95u4b7v"   # my token


def notifySqr(message):
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": api_token,
      "user": user_key,
      "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
message_content = "github message at " + current_time

notifySqr(message_content)
