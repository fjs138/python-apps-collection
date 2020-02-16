import urllib.request
import time
# import twitter


# twitter authentication
# CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx' # Same as API key
# CONSUMER_SECRET is analogous to API secret
# CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# ACCESS_TOKEN_KEY= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# ACCESS_TOKEN_SECRET= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# Line length limit should be 72 characters---------------------------->

# This function retrieves the coffee price from a website
def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    text = page.read().decode("utf8")
    where = text.find("$")
    startOfPrice = where + 1
    endOfPrice = startOfPrice + 4
    return float(text[startOfPrice:endOfPrice])


# This function updates the status of my twitter account but it is deprecated
# def send_to_twitter(msg):
#     msg = "I am a message that will be sent to Twitter"
#     password_manager = urllib.request.HTTPPasswordMgr()
#     password_manager.add_password("Twitter API",
#                                   "https://api.twitter.com/1/statuses/", "xxxxxxx", "xxxxxxx")
#     http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
#     page_opener = urllib.request.build_opener(http_handler)
#     urllib.request.install_opener(page_opener)
#     params = urllib.parse.urlencode( {'status': msg} )
#     resp = urllib.request.urlopen("https://api.twitter.com/1.1/statuses/update.json", params)
#     resp.read()



# This function updates the status of my twitter account requires twitter python module
# def send_to_twitter(status_msg):
#     if len(status_msg) > 140 :
#         raise Exception ('Status message too long !!!')
#     else:
#         authkey = t.Twitter(auth=t.OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
#         result = authkey.statuses.update(status=status_msg)
#         return result

price = 9.99

needPriceNow = input("Is this price needed now (y/n)?")
price = get_price()
if needPriceNow =="y":
    print(get_price())
   # status_msg = str(get_price())
   # send_to_twitter()
    print ("Buy!")
else:
    price = 9.99
    while price > 4.74:
        # price = float(price)
        # price=text[234:238]
        # if price > 4.74:
        price=get_price()
        if price > 4.74:
            time.sleep(900)
        else:
            print("Buy!")
            # send_to_twitter()
