#Endpoint == URL

#------------------------------------------------------------------------------------------------------------------------------------
#                               Packages installed
#------------------------------------------------------------------------------------------------------------------------------------

from twitter import Twitter,OAuth
import pprint
import tweepy
import textblob
from textblob import TextBlob

#------------------------------------------------------------------------------------------------------------------------------------
#                               Function to count the numbers of followers
#------------------------------------------------------------------------------------------------------------------------------------

get_num_followers(query):
    import json
    num_followers = 0
    tweets = get_tweets(query)
    for each_tweet in tweets[]:
        print(each_tweet['user']['followers_count'])
        num_followers = += each_tweet['user']['followers_count']
    return num_followers

#------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------

def get_tweets(query):
    tweets = twitter.search.tweets(q='#' + query)
    return tweets

#------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------

oauth = tweepy.OAuthHandler(API_KEY,API_SECRET)
b = tweepy.OAuthHandler('134','213')
oauth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(oauth)
public_tweets = api.search("#DeleteFacebook")
new_tweets = api.user_timeline(screen_name = '@DonalTrump',max_id=oldest)
for tweet in new_tweets:
    print(tweet.text)
    analyse = TextBlob(tweets.text)
    print(analyse,sentiment)
    print("-----------------")

#------------------------------------------------------------------------------------------------------------------------------------
#                   Determine the Sentiment of People tweeting using a certain hashtag
#------------------------------------------------------------------------------------------------------------------------------------

for tweet in public_tweets:
    print(tweet.text)
    print(tweet.created_at)
    print(tweet.author)
    analyse = TextBlob(tweets.text)
    print(analyse,sentiment)
    print("-----------------")

#------------------------------------------------------------------------------------------------------------------------------------


alltweets = []
alltweets.extend(new_tweets)




























#------------------------------------------------------------------------------------------------------------------------------------
#                                          Main function program
#------------------------------------------------------------------------------------------------------------------------------------
def main():
    while(True):
        user_choice = raw_input("1. Count the followers of people tweeting using a certain hashtag.\n"
                                "2. Determine the location, Timezone and language of people tweeting using a certain hashtag.\n"
                                "3. Number of times Modi has referred to US in the past 200 Tweets compared to how man...\n"
                                "4. Determine the Sentiment of People tweeting using a certain hashtag.\n"
                                "5. Top used words by PM Modi on Twitter.\n"
                                "6. Tweet a message from your account.\n"
                                "7. Exit\n")
        if user_choice == 1:
            user_input = raw_input("Enter the Hashtag: ")
            print("\n\n Max. number of people who might have seen this hashtag: %s" %(get_num_followers(user_input)))

        elif user_choice == 2:
            user_input = raw_input("Enter the Hashtag: ")
            demographic_data(user_input)

        elif user_choice == 3:
            ModiVSTrump()

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

main()
# Credentials of the developer for calling the Twitter API

# NOT THE CORRECT ACTUAL KEYS
API_KEY = '	Djhgbjjhgjjgjhhgjne9yryP'
API_SECRET = 'agoifghfhfuyfjhgjyhtuygvjhgyu5EERAnbj'
ACCESS_TOKEN = '84542986786785875-vjfkthfvjhftyR54ksm86K8'
ACCESS_TOKEN_SECRET = 'zaZqWnckwndfkjsncksdncBifY37wMGFoM9kX'

#The permissions returned by the OAuth class of twitter package in the form of object
twitter_oouth = OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,API_KEY,API_SECRET)

#OAuth puts the parameters to HTTP headers
#HTTP HEADER

twitter = Twitter(auth=twitter_oouth)
#twitter class object used to call the API

results = twitter.search.tweet(q='digital forensics', geography='28.6315 77.2167 20km')
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)

#1. Search for a hashtag and then determine the total count of the followers of the people who tweeted using that hashtag


#2. Determine the demographic(gender,timezone,locale) of people who have tweet using certain hash tag

