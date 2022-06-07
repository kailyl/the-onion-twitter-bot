import tweepy
from main import main_func


consumer_key = 'sw24Mq7sMbbbDXnQvO2v282FW'
consumer_secret = 'e9WXBfYYAfgFAVqPvL05WCIcxN62empvNWJlAo2KWK3UHJ047f'
access_token = '1533593322819821569-RoMRfA6w7h0BteSLAalyqsUcoApKr1'
access_token_secret = '7Xmx1dQappgz7lEJCS75lgv8OJZskH18c25CLMblJY6CW'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = main_func()

api.update_status(tweet)
print(tweet)