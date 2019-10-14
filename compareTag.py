consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""


import tweepy
import numpy as np
from textblob import TextBlob


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


def compareSentiment(tag1,tag2):
    tweets = twitter.search(tag1)
    analysis1=[]
    for tweet in tweets:
        analysis1.append(TextBlob(tweet.text).sentiment.polarity)
    tweets = twitter.search(tag2)
    analysis2=[]
    for tweet in tweets:
        analysis2.append(TextBlob(tweet.text).sentiment.polarity)
    if np.average(analysis1)>np.average(analysis2):
        return tag1
    return tag2
    
tag1=''
tag2=''

tag1=input('Please input First Tag ')
tag2=input('Please input Second Tag ')

print("This tag has more good views => ",compareSentiment(tag1,tag2))
