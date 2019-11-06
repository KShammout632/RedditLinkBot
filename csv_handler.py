import reddit_bot, file_handle
import csv


def addToCSV():
    loc = reddit_bot.getCDetails()
    # Assumes there is a file called 'comment_details.csv' in the directory
    with open('comment_details.csv', 'a', encoding='utf-8') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Subreddit', 'Karma'])
        for c in loc:
            filewriter.writerow(c)


total_c = file_handle.get_popular_comments() + file_handle.get_unpopular_comments()

addToCSV()
