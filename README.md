# buildABot
basic files to build a twitter bot

This uses python code to use twitter API to read/post tweets

Requirements:
* twitter developer account: Fill out developer application ([here](https://developer.twitter.com))
* Python tweepy library: install the library with the following command `python -m pip install tweepy`
* Python datetime library: install the library with the following command `python -m pip install datetime`

### Clone this repository

Use the command `git clone https://github.com/kwraight/buildABot.git`

You should now have a directory `buildABot`. Go in and start the fun!

### Send a tweet

Start by updating the APIsettings file with your own credentials. 
  * open the file
  * edit the text `YOUR_INFO_HERE` with appropriate info from twitter development website
  * save the file
Post the tweet using the following command: `python postTweet.py`
  * tweet should be of the form `This tweet was posted at: SOMETIME`
