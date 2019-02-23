"""
PROGRAM: STREAMS TWITTER FOR GIVEN KEYWORDS --> SAVES THE TWEETS W/ KEYWORDS --> FAVORITES THE TWEETS
OUTPUT: (1) API.FAVORITES(TWEETS) (2) FILE CONTAING TWEETS IN JSON FORMAT

CREATED: 17 Feb 2017
MODIFIED: 02 May 2017
MODIFIED: 12 May 2017

AUTHOR: PriyankaSadhukhan

"""


# methods from tweepy library
import os
import sys
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import datetime



# TWITTER ACCOUNT CREDENTIALS: 
consumer_key= ''				
consumer_secret= ''
access_token='-ehCOMKuX2FGya2m0YfeusWWwyg647yr'
access_token_secret=''


startTime = datetime.datetime.now().strftime('%d%m%Y-%H%M%S')
f = open(startTime, 'w')	#save file name !!!

Locations = ('India', 'Mumbai', 'Navi Mumbai', 'Bengaluru', 'Bangalore', 'Delhi', 'Chennai', 'Kolkata', 'Pune', 'Goa')
Fav_IDs = []

# pritnt tweets
class StdOutListener(StreamListener):
	def on_data(self, data):
		print(data, file=f)
		tweetJSON = json.loads(data)
		tweetID = tweetJSON['id']
		for location in Locations:
			if tweetJSON['user']['location'] is not None and location in tweetJSON['user']['location']:
				Fav_IDs.append(tweetID)
				#print(tweetJSON['user']['location'], Fav_IDs, sep="\t")
				try:
					api.create_favorite(tweetID)
				except:
					pass
				
			break
		print(datetime.datetime.now(), tweetJSON['text'], tweetJSON['user']['location'], sep="\t")
		return True
	def on_error(self, status):
                print(status, file=f)


if __name__ == '__main__':

    # Twitter authetification and the connection and Twitter Streaming API
    lis = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, lis)
    api = tweepy.API(auth)

    # filter Tweets by keywords
    stream.filter(track=['modular synth','modular synthesizer','twigttsoip','modular analog','modularanalog', 'synth', 'korg', 'volca', 'synthesizer', 'arturia', 'moog', 'doepfer', 'electronic music', 'microbrute', 'minibrute', 'drumbrute']) #

f.close()
