import tweepy
import json
import pandas as po

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = input("Enter user: ")
target_timeline = api.user_timeline(screen_name = user, count = 100)

tweets_list = list()
for tweet in target_timeline:
    jsonresponse = tweet._json
    #jsonobject = json.loads(jsonresponse)
    #print(json.dumps(jsonobject, indent=1))
    #print(jsonresponse)
    tweets_list.append(jsonresponse)

dataframe = po.DataFrame(tweets_list)
dataframe.to_json('tweets_data.json')
#print(dataframe)
dataframe.to_csv('tweets_data.csv')

with open('tweets_data.json', 'r') as json_file:
    json_object = json.load(json_file)

print(json.dumps(json_object, indent=1)) #prints json data in pretty text in output terminal
