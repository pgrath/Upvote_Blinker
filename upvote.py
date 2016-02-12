import praw

#set up user agent and select user 
r = praw.Reddit(user_agent='Upvote_blinker')

usr = r.get_redditor('hofnbricl')

#easy stuff here
totalKarma = usr.comment_karma + usr.link_karma

print(totalKarma)
