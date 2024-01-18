import praw
import pandas as pd

# Initialise connection to Reddit API
reddit = praw.Reddit(client_id='', client_secret='',
                     user_agent='Political Leaning')

# Take top posts from subreddit
subreddit_top_posts = reddit.subreddit("ukpolitics").top(limit=100)

# Initialise titles and comments arrays
post_titles = []
post_comments = []
post_authors = []
post_time_created = []
post_score = []
post_is_submitter = []
post_author_comment_karma = []

# Collects all comments on each post collected from the r/tories subreddit
for post in subreddit_top_posts:
    submission = reddit.submission(id=post.id)

    submission.comments.replace_more(limit=None)
    for top_comments in submission.comments.list():
        post_titles.append(post.title)
        post_comments.append(top_comments.body)
        post_authors.append(top_comments.author)
        post_time_created.append(top_comments.created_utc)
        post_score.append(top_comments.score)
        post_is_submitter.append(top_comments.is_submitter)

# Arrays are put into a dataframe and converted into a csv
dataframe = pd.DataFrame()
dataframe["Title"] = post_titles
dataframe["Comment"] = post_comments
dataframe["Redditor"] = post_authors
dataframe["Time Posted UTC"] = post_time_created
dataframe["Comment Karma"] = post_score
dataframe["Commenter is OP"] = post_is_submitter

# Remove all comments with a deleted author
dataframe = dataframe.dropna(axis=0, subset=["Author"])

dataframe.to_csv("UK Politics.csv")
