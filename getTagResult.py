consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""


import tweepy
import numpy as np
from textblob import TextBlob


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


def getSentiment(tag):
    tweets = twitter.search(tag)
    analysis=[]
    for tweet in tweets:
        analysis.append(TextBlob(tweet.text).sentiment.polarity)
    return np.average(analysis)
    
tag=''
tag=input()
print(getSentiment(tag))
