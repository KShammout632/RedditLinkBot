import config
import os

def create_file(filename):
	if os.path.isfile(filename):
		print (os.path.dirname(filename))
		return filename
	else:
		file = open(filename, 'w')			#Creates the file if it doesnt exist
		print(filename, "was created")
		file.close()
		create_file(filename)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		create_file("comments_replied_to.txt")
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			#comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

def get_popular_comments():
	if not os.path.isfile("popular_comments.txt"):
		create_file("popular_comments.txt")
		popular_comments = []
	else:
		with open("popular_comments.txt", "r") as f:
			popular_comments = f.read()
			popular_comments = popular_comments.split("\n")

	return popular_comments

def get_unpopular_comments():
	if not os.path.isfile("unpopular_comments.txt"):
		create_file("unpopular_comments.txt")
		unpopular_comments = []
	else:
		with open("unpopular_comments.txt", "r") as f:
			unpopular_comments = f.read()
			unpopular_comments = unpopular_comments.split("\n")

	return unpopular_comments
