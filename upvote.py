import praw
import time
import piglow

#set up user agent and select user 
r = praw.Reddit(user_agent='Upvote_blinker')
usr = r.get_redditor('reddit_user')

#set up piglow
piglow.auto_update = True
piglow.clear_on_exit = True

#get the karma
def getKarma():
    totalKarma = usr.comment_karma + usr.link_karma
    return totalKarma

#function to make the piglow glow
def glow():
	for p in range(2):
		for x in range(255):
			piglow.arm(0, x)
			piglow.arm(1, x)
			piglow.arm(2, x)

		for x in reversed(range(255)):
			piglow.arm(0, x)
			piglow.arm(1, x)
			piglow.arm(2, x)




#get initial karma value
karmaScore = getKarma()

while True:
    #get most recent karma score, then inform the user if it is greater than the initial value
    currScore = getKarma()
    if karmaScore < currScore:
        print("Upvote detected!")
        karmaScore = currScore
	glow()
    else:
        continue

    time.sleep(5)
