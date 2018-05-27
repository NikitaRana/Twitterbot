#Endpoint == URL

# Credentials of the developer for calling the Twitter API
API_KEY = '	DtAQYZdw4ncGZvhrFEne9yryP'
API_SECRET = 'ygoiqvhQ1Vxrv2JXlFAuxeXVmoQNgqegq2KbbLd2YS5EERAnbj'
ACCESS_TOKEN = '885825714510888960-r63kAG7GMUyRGM0cIDPfSR54ksm86K8'
ACCESS_TOKEN_SECRET = 'zaZqWTEHYFFjVJfDBhl4QV5rai4ULfBifY37wMGFoM9kX'

from twitter import Twitter,OAuth
import pprint

#The permissions returned by the OAuth class of twitter package in the form of object
twitter_oouth = OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,API_KEY,API_SECRET)

#OAuth puts the parameters to HTTP headers
#HTTP HEADER

twitter = Twitter(auth=twitter_oouth)
#twitter class object used to call the API

results = twitter.search.tweet(q='digital forensics',geography = '28.6315 77.2167 20km')
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)
