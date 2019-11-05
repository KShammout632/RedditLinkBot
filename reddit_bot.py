import praw
import config
import time
import os
import file_handle

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "My robot test v0.1")
	print ("Logged in!")

	return r

def run_bot(r, comments_replied_to):
	for comment in r.subreddit('popular').comments(limit=800):
		if ("link?" in comment.body or "Link?" in comment.body) and comment.id not in comments_replied_to and comment.author != r.user.me():
			print ("Link String found: " + comment.id)
			print(comment.body)
			if(not comment.submission.over_18):
				comment.reply("[Here you go!](https://www.ssbwiki.com/images/thumb/2/23/HWL_Toon_Link_Artwork.png/1200px-HWL_Toon_Link_Artwork.png)")
				print ("Replied to comment")
			else:
				print("Submission ID: " + comment.submission.id)
				print ("NSFW post. Did not reply.")

			time.sleep(6)

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	#print (comments_replied_to)

	print ("Sleep for 5 seconds")
	#time.sleep(5)

def secondary():
	try:
		while True:
			run_bot(r, comments_replied_to)

	except:
		traceback.print_exc()
		print('Resuming in 30sec...')
		time.sleep(30)

def checkPopularity():
	c_list = r_redditor.comments.new(limit=None)
	for comment in c_list:										# iterates through ResVenBot's comments
		if comment not in popular_comments and comment not in unpopular_comments and (time.time() - comment.created_utc > 86400):
			if comment.score > 0:
				popular_comments.append(comment.id)				# adds the comment id to the array
				with open ("popular_comments.txt", "a") as f:	# adds the comment id to the file
					f.write(comment.id + "\n")
			else:
				unpopular_comments.append(comment.id)
				with open ("unpopular_comments.txt", "a") as f:
					f.write(comment.id + "\n")

def getCDetails():
	c_list = r_redditor.comments.new(limit=None)
	retList = []
	for comment in c_list:
		#parent = comment.parent()
		#submission = comment.submission
		sb = comment.subreddit			# subreddit replying to
		#desc = parent.body				# comment body replying to
		#scp = parent.score				# parent comment's score
		scc = comment.score				# bot comment's score
		#title = submission.title		# title of submission
		att = [sb,scc]
		retList.append(att)
		print(retList)

	return retList


r = bot_login()									# r is an instance of Reddit
r_user = r.user
r_redditor = r.redditor('ResVenBot')
comments_replied_to = file_handle.get_saved_comments()
popular_comments = file_handle.get_popular_comments()
unpopular_comments = file_handle.get_unpopular_comments()

for num in range(1,2):
	checkPopularity()
	secondary()
