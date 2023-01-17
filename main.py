import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

apikey = "Nb4LS27vWyqRQn9BOFFMXvJrc"
api_secret = "Njs9QbkkyzCH58YdsKC4e6nQ1yiXchH3bmdCczDQjBrOGUN8eG"
api_access = "1575069975479390209-z9AJIRXT3eBrQWIT3u8HRf5uVMvvKD"
api_access_secret = "ROVJ6XtK4qDSTV8NYR3hdiIPSg9ogclR3tcfkDOs42tQd"

auth = tweepy.OAuthHandler(consumer_key=apikey, consumer_secret=api_secret)
auth.set_access_token(api_access, api_access_secret)


###SEARCH TOPICS
api=tweepy.API(auth)

tweets=tweepy.Cursor(api.search_tweets,"death").items(100)

def cleantext(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    return text
polarity=0
p=0
n=0
N=0

for i in tweets:
    text=cleantext(i.text)
    analysis = TextBlob(text)
    polarity=analysis.polarity
    if polarity>0:
        p+=1
    elif polarity==0:
        n+=1
    else:
        N+=1


   # print(text)
print(p,n,N)

###SEARCH USERS
# api = tweepy.API(auth, wait_on_rate_limit=True)
# posts = api.user_timeline(screen_name="elonmusk", count=100, tweet_mode="extended")
#
# dataframe = pd.DataFrame([i.full_text for i in posts], columns=["Tweets"])
# dataframe.head()
#
#

#
#
# dataframe['Tweets'] = dataframe['Tweets'].apply(cleantext)
# #print(dataframe)
#
#
# def getsubjecitivty(text):
#     return TextBlob(text).sentiment.subjectivity
#
#
# def getPolarity(text):
#     return TextBlob(text).sentiment.polarity
#
#
# dataframe['Subjectivity'] = dataframe['Tweets'].apply(getsubjecitivty)
# dataframe['Polarity']=dataframe['Tweets'].apply(getPolarity)
# #print(dataframe)
#
# allwords=' '.join(tweets for tweets in dataframe['Tweets'])
# wordcloud = WordCloud(width=500,height=300,random_state=21,max_font_size=110).generate(allwords)
# #print(wordcloud)
# plt.imshow(wordcloud,interpolation="bilinear")
# plt.axis('off')
# #plt.show()
#
#
# def getAnalysis(score):
#     if score<0:
#         return 'Negative'
#     elif score==0:
#         return 'Neutral'
#     else:
#         return 'Positive'
#
# dataframe['Analysis']=dataframe['Polarity'].apply(getAnalysis)
# #print(dataframe)
#
# # sorteddataframe = dataframe.sort_values(by=['Polarity'])
# # #print(sorteddataframe)
# # for i in range(sorteddataframe.shape[0]):
# #     if(sorteddataframe['Analysis'][i]=='Positive'):
# #         print(sorteddataframe['Tweets'][i])
# #
# # sorteddataframe = dataframe.sort_values(by=['Polarity'],ascending="False")
# # #print(sorteddataframe)
# # for i in range(sorteddataframe.shape[0]):
# #     if(sorteddataframe['Analysis'][i]=='Negative'):
# #         print(sorteddataframe['Tweets'][i])
#
# plt.figure(figsize=(8,6))
# for i in range(dataframe.shape[0]):
#     plt.scatter(dataframe['Polarity'][i],dataframe['Subjectivity'][i],color="Blue")
# plt.title("Sentiment Analysis")
# plt.xlabel('Polarity')
# plt.ylabel('Subjectivity')
# #plt.show()
#
#
# ptweets=dataframe[dataframe.Analysis=="Positive"]
# ptweets=ptweets['Tweets']
# print(ptweets.shape[0]/dataframe.shape[0])
# ntweets=dataframe[dataframe.Analysis=="Negative"]
# ntweets=ntweets['Tweets']
# print(ntweets.shape[0]/dataframe.shape[0])
# ntweets=dataframe[dataframe.Analysis=="Neutral"]
# ntweets=ntweets['Tweets']
# print(ntweets.shape[0]/dataframe.shape[0])