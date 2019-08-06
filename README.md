# buildABot
Basic files to build a twitter bot -  using python code with twitter API to read/post tweets.

The following instructions assume you're using a raspberry-pi (or some linux like system).

Requirements:
* twitter developer account: Fill out developer application [here](https://developer.twitter.com) (check out some online [instruction](http://docs.inboundnow.com/guide/create-twitter-application/))
* Python *tweepy* library: install the library with the following terminal command `python -m pip install tweepy`
* Python *datetime* library: install the library with the following terminal command `python -m pip install datetime`

### Open a terminal

Navigate the pointy-clicky thing to the raspberry icon (top-left of desktop screen). From the drop down menu select `Accessories` then `Terminal`. 
(You may also have the terminal icon on the taskbar.)

Welcome to the matrix!

### Clone this repository

We'll use the *git* to download the code so first make sure you got the *git*.

In the terminal check you have *git* using the command: `which git`. 
  * If you get a program path back, e.g. `/usr/bin/git`,  you're good to go.
  * If you got nothing then you need to install *git*: use the command `sudo apt-get install git`, then say yes to any questions asked.
  
Now you should have *git*.

Use the terminal command `git clone https://github.com/kwraight/buildABot.git`

You should now have a directory `buildABot`. 
  * List the directories using teminal command `ls`
  * Change into directory using terminal command `cd buildABot`

Go in and start the fun!

### Send a tweet

There are two important files for this part:
  * *APIsettings.py* will handle the authentication of the account and setting up the API, the portal to twitter.
  * *postTweet.py* will use one of the built in API functions to send a tweet. 

Start by updating the *APIsettings.py* file with your own credentials. 
  * Open the file, e.g. `emacs APIsettings.py &`. A text editor window should pop up with the code inside.
  * Replace the text `YOUR_INFO_HERE` with appropriate info from twitter development website.
  * Save the file: click the icon what looks like a disc.

The *postTweet.py* file is where the 
Post the tweet using the following command: `python postTweet.py`
  * There should be a tweet from your account with the form `This tweet was posted at: SOMETIME`

Congratulations, now you have the basics for using twitter from a terminal.

### Read a tweet

Now to get some data.  Reading is similar in that it uses the API, your portal to twitter, but what skill lies in what you do with the data gleaned.


