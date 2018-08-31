# template for setting API credentials

# included libraries
import tweepy # twitter API library


# fill in the values of theis variable with twitter API credentials
cfg = {
    "consumer_key"        : "YOUR_INFO_HERE",
    "consumer_secret"     : "YOUR_INFO_HERE",
    "access_token"        : "YOUR_INFO_HERE",
    "access_token_secret" : "YOUR_INFO_HERE"
}

# this function defines API (using the tweepy library) to return an api object ready to use
def get_api():
    # use cfg variable from above
    global cfg
    # set-up API object
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    # return the set-up API object
    return tweepy.API(auth)

