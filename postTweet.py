# post a simple tweet (some text and time) to twitter

# included libraries
import tweepy # twitter API library
from datetime import datetime, date, timedelta # useful for getting the time
import APISettings # this is the file where credentials are set

# this function posts the tweet
def postInfo(val, type, id):
    #get the api object definition from the other file
    api=APISettings.get_api()
    # deine the tweet: some text and the time
    tweet = "This tweet was posted at:"+str(datetime.now()) # add time to avoid repeated tweets
    # print to screen what the tweet will say. This will appear in the terminal as you run the code
    print tweet
    # post it!
    status = api.update_status(status=tweet)

# the main function, the numero uno, the prima... thing
if __name__ == "__main__":
    main()

