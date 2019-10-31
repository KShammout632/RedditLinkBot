import praw
import config
import time
import os

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "My robot test v0.1")
	print ("Logged in!")

	return r

def run_bot(r, comments_replied_to):
	#print ("Obtaining comments")

	for comment in r.subreddit('all').comments(limit=800):
		if ("link?" in comment.body or "Link?" in comment.body) and comment.id not in comments_replied_to and comment.author != r.user.me():
			print ("Link String found " + comment.id)
			print(comment.body)
			comment.reply("[Here you go!](https://www.ssbwiki.com/images/thumb/2/23/HWL_Toon_Link_Artwork.png/1200px-HWL_Toon_Link_Artwork.png)")
			print ("Replied to comment ")
			time.sleep(6)

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

		if ("mirror?" in comment.body or "Mirror?" in comment.body) and comment.id not in comments_replied_to and comment.author != r.user.me():
			print ("Mirror String found " + comment.id)
			print(comment.body)
			comment.reply("[Here you go!](https://s-media-cache-ak0.pinimg.com/736x/d2/a4/1c/d2a41c03f5dcab554f143f65fc1551d7.jpg)")
			print ("Replied to comment ")
			time.sleep(6)

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	#print (comments_replied_to)

	print ("Sleep for 5 seconds")
	#Sleep for 5 seconds
	time.sleep(5)

def secondary():
	try:
		while True:
			run_bot(r, comments_replied_to)

	except:
		traceback.print_exc()
		print('Resuming in 30sec...')
		time.sleep(30)

def create_file():
	if os.path.isfile("comments_replied_to.txt"):
		print (os.path.dirname("comments_replied_to.txt"))
		return "comments_replied_to.txt"
	else:
		#Creates the file if it doesnt exist
		file = open("comments_replied_to.txt", 'w')
		print("comments_replied_to.txt", "was created")
		file.close()
		create_file()

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		create_file()
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			#comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print (comments_replied_to)

for num in range(1,2):
	secondary()
	#run_bot(r, comments_replied_to)
	#runAllPosts(r)
