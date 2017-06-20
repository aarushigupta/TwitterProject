from keys import *
import tweepy

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

searchQuery = '#yoga'
tweetsPerQry = 100

tweets = api.search(q=searchQuery, count=tweetsPerQry)

print tweets[1]
