#Endpoint == URL

def main():
    while(True):
        user_choice = raw_input("1. Count the followers of people tweeting using a certain hashtag.\n"
                                "2. Determine the location, Timezone and language of people tweeting using a certain hashtag.\n"
                                "3. Number of times MOdi has referred to US in the past 200 Tweets compared to how man...\n"
                                "4. Determine the Sentiment of People tweeting using a certain hashtag.\n"
                                "5. Top used words by PM Modi on Twitter.\n"
                                "6. Tweet a message from your account.\n"
                                "7. Exit\n")
        if user_choice == 1:
           user_input = raw_input("Enter the Hashtag: ")
            get_num_followers(user_input)

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
API_KEY = '	DtAfdansjfZdw4fsdgvdgdgvdsncGZvhrFEne9yryP'
API_SECRET = 'ygoiqvhQ1Vxrv2JXlFAuxeXgsdgdsgvdfgdsvfsfsVmoQNgqegq2KbbLd2YS5EERAnbj'
ACCESS_TOKEN = '885jfkshdfiu589374548397983093sm86K8'
ACCESS_TOKEN_SECRET = 'z840239374903275983nkjfsdoifhewoifskX'

from twitter import Twitter,OAuth
import pprint

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

