import praw
import pandas as pd

# Initialise connection to Reddit API
reddit = praw.Reddit(client_id='', client_secret='',
                     user_agent='Political Leaning')

# Take top 500 posts from r/tories and r/laboruk
tories_top_posts = reddit.subreddit("tories").top(limit=500)
labouruk_top_posts = reddit.subreddit("labouruk").top(limit=500)

# Initialise titles and comments arrays
post_titles = []
post_comments = []

# Collects all comments on each post collected from the r/tories subreddit
for post in tories_top_posts:
    submission = reddit.submission(id=post.id)

    submission.comments.replace_more(limit=10)
    for top_comments in submission.comments.list():
        post_titles.append(post.title)
        post_comments.append(top_comments.body)

# Collects all comments on each post collected from the r/labouruk subreddit
for post in labouruk_top_posts:
    submission = reddit.submission(id=post.id)

    submission.comments.replace_more(limit=10)
    for top_comments in submission.comments.list():
        post_titles.append(post.title)
        post_comments.append(top_comments.body)

# Arrays are put into a dataframe and converted into a csv
dataframe = pd.DataFrame()
dataframe["Title"] = post_titles
dataframe["Comments"] = post_comments

dataframe.to_csv("Naively Labelled Political Comments and their Leaning.csv")
