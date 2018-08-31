# buildABot
basic files to build a twitter bot

This uses python code to use twitter API to read/post tweets.

Requirements:
* twitter developer account: Fill out developer application [here](https://developer.twitter.com) (check out some online [instruction](http://docs.inboundnow.com/guide/create-twitter-application/))
* Python tweepy library: install the library with the following terminal command `python -m pip install tweepy`
* Python datetime library: install the library with the following terminal command `python -m pip install datetime`

### Clone this repository

Use the terminal command `git clone https://github.com/kwraight/buildABot.git`

You should now have a directory `buildABot`. 
  * list the directories using teminal command `ls`
  * change into directory using terminal command `cd buildABot`
  
Go in and start the fun!

### Send a tweet

Start by updating the APIsettings file with your own credentials. 
  * open the file, e.g. `emacs APIsettings.py`
  * edit the text `YOUR_INFO_HERE` with appropriate info from twitter development website
  * save the file
Post the tweet using the following command: `python postTweet.py`
  * tweet should be of the form `This tweet was posted at: SOMETIME`

Congratulations, now you have the basics for using twitter from a terminal.
