import tweepy

print("This is my twitter bot")

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = '-'
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# this api will be used to communicate with twitter
api = tweepy.API(auth)
mentions = api.mentions_timeline()
print(mentions)
