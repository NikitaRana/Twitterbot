#------------------------------------------------------------------------------------------------------------------------------------
#                    List of packages imported
#------------------------------------------------------------------------------------------------------------------------------------

from twitter import Twitter,OAuth
import pprint
import tweepy
import textblob
from textblob import TextBlob
import json

#------------------------------------------------------------------------------------------------------------------------------------
#                       Inclusions of files
#------------------------------------------------------------------------------------------------------------------------------------

global f
global f2
f = open('positive.txt','w')
f2 = open('negative.txt','w')

#------------------------------------------------------------------------------------------------------------------------------------
#                    Function to search for tweets
#------------------------------------------------------------------------------------------------------------------------------------
tweets = []
def GetSearch(query):
    tweets = twitter.search.tweets(q='#' + query)
    return tweets

#------------------------------------------------------------------------------------------------------------------------------------
#                    Function to count the numbers of followers
#------------------------------------------------------------------------------------------------------------------------------------

def Get_number_followers(query):
    num_followers = 0
    tweets = GetSearch(query)
    for each_tweet in tweets[]:
        print(each_tweet['user']['followers_count'])
        num_followers += each_tweet['user']['followers_count']
    return num_followers

#------------------------------------------------------------------------------------------------------------------------------------
#                   Function to determine the location,language and time zone
#------------------------------------------------------------------------------------------------------------------------------------
def Demographic_data ( user_input ):
    tweets = GetSearch(user_input)
    for each_tweet in tweets:
        print(each_tweet['user']['location'])
        print(each_tweet['user']['timezone'])
        print(each_tweet['user']['language'])

#------------------------------------------------------------------------------------------------------------------------------------
#                   Function to determine the location,language and time zone
#------------------------------------------------------------------------------------------------------------------------------------
def  ModiVSTrump():
    oauth = tweepy.OAuthHandler(API_KEY,API_SECRET)
    b = tweepy.OAuthHandler('134','213')
    times = 0
    oauth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api = tweepy.API(oauth)
    public_tweets = api.search("#US")
    new_tweets = api.user_timeline(screen_name = '@Modi',count=200)
    for tweet in new_tweets:
        print(tweet.text)
        times+=times
    return  times

#------------------------------------------------------------------------------------------------------------------------------------
#                    Function to determine the sentimment
#------------------------------------------------------------------------------------------------------------------------------------
def sentiment_analysis(query):

    oauth = tweepy.OAuthHandler(API_KEY,API_SECRET)
    b = tweepy.OAuthHandler('134','213')
    oauth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api = tweepy.API(oauth)
    public_tweets = api.search("query")
    new_tweets = api.user_timeline(screen_name = '@DonalTrump',max_id=oldest)
    for tweet in new_tweets:
        print(tweet.text)
        analyse = TextBlob(tweets.text)
        print(analyse,sentiment)
        print("-----------------")
        if analysis.sentiment.polarity > 0:
            f.write ( "This is positive:> \n" + tweet )
        elif analysis.sentiment.polarity == 0:
            f2.write ( "This is Negative:> \n" + tweet )
        else:
            print("Well if its less then its a problem")

#------------------------------------------------------------------------------------------------------------------------------------
#                   Function to determine top usage of words
#------------------------------------------------------------------------------------------------------------------------------------
def ModiTopWords():
    oauth = tweepy.OAuthHandler ( API_KEY, API_SECRET )
    b = tweepy.OAuthHandler ( '134', '213' )
    oauth.set_access_token ( ACCESS_TOKEN, ACCESS_TOKEN_SECRET )
    api = tweepy.API ( oauth )
    public_tweets = api.search ( "#DeleteFacebook" )
    new_tweets = api.user_timeline ()
    for tweet in new_tweets:
        print(tweet.text)

#------------------------------------------------------------------------------------------------------------------------------------
#                                          Function to tweet a message
#------------------------------------------------------------------------------------------------------------------------------------

##def add_tweet(query):

#------------------------------------------------------------------------------------------------------------------------------------
#                                          Main function program
#------------------------------------------------------------------------------------------------------------------------------------
def main():
    while(True):
        user_choice = raw_input("1. Count the followers of people tweeting using a certain hashtag.\n"
                                "2. Determine the location, Timezone and language of people tweeting using a certain hashtag.\n"
                                "3. Number of times Modi has referred to US in the past 200 Tweets\n"
                                "4. Determine the Sentiment of People tweeting using a certain hashtag.\n"
                                "5. Top used words by PM Modi on Twitter.\n"
                                "6. Tweet a message from your account.\n"
                                "7. Exit\n")
        if user_choice == 1:
            user_input = raw_input("Enter the Hashtag: ")
            print("\n\n Max. number of people who might have seen this hashtag: %s" %(Get_number_followers(user_input)))

        elif user_choice == 2:
            user_input = raw_input("Enter the Hashtag: ")
            Demographic_data(user_input)

        elif user_choice == 3:
            print("\n\nNumber of times Modi mentioned US in the past 200 tweets are %s" %ModiVSTrump())

        elif user_choice ==4:
            user_input = raw_input ( "Enter the Hashtag: " )
            sentiment_analysis(user_input)

        elif user_choice ==5:
            ModiTopWords()

        elif user_choice ==6:
            user_input = raw_input("Enter the Tweet: ")
            add_tweet(user_input)

        elif user_choice == 7:
            break

        else:
            print("I didn't get that. Please try again. ")

def main():
    if __name__ == '__main__':
        main()
# Credentials of the developer for calling the Twitter API

# THESE ARE INCORRECT KEYS-------------V

API_KEY = '	Wfjwisfjewkjfwoine9yryP'
API_SECRET = 'nweknfdklasndkwefeXVmoQfmklewnfkwHKJHEKDWnbj'
ACCESS_TOKEN = '345578423374982-r63kAG7GMUyRGM0cIDPfSR54ksm86K8'
ACCESS_TOKEN_SECRET = '4289375293873nckdsnnkjshcskfBifY37wMGFoM9kX'

# THESE ARE INCORRECT KEYS--------------^


#The permissions returned by the OAuth class of twitter package in the form of object
twitter_oouth = OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,API_KEY,API_SECRET)

#OAuth puts the parameters to HTTP headers
#HTTP HEADER

twitter = Twitter(auth=twitter_oouth)
#twitter class object used to call the API

results = twitter.search.tweet(q='digital forensics', geography='28.6315 77.2167 20km')
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)


