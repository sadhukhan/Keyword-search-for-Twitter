# code2 tweet data from json file

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
#import Textblob

  
tweets_data_path = '.\\downstairs\\res1300hrs20Feb2017_india.json'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
#print('Twitter Handle', 'Tweet/RT', 'User location', 'Original Tweet by', sep='\t') # 'User Description',
for line in tweets_file:
	try:
		tweet = json.loads(line)
		#print(tweet['user']['screen_name'], tweet['text'], tweet['user']['location'], sep='\t')	# tweet['user']['description'],
		print(tweet['user']['screen_name'])
		tweets_data.append(tweet)
	except:
		continue
		
	#analysis = Textblob(tweet)
	#print(len(tweets_data))
	
"""
15Feb2017
printing works amazingly now
now need to tokenize and write script for trending topics
trending topics = most used words,  most used hashtags
					most used combination of words



tweets = pd.DataFrame()		#pandas

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
"""
