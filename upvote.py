import praw
import time

#set up user agent and select user 
r = praw.Reddit(user_agent='Upvote_blinker')

usr = r.get_redditor('hofnbricl')

#get the karma
def getKarma():
    totalKarma = usr.comment_karma + usr.link_karma
    return totalKarma

#get initial karma value
karmaScore = getKarma()

while True:
    #get most recent karma score, then inform the user if it is greater than the initial value
    currScore = getKarma()
    if karmaScore < currScore:
        print("Upvote detected!")
        karmaScore = currScore
    else:
        continue

    time.sleep(5)
