import praw
import pandas as pd

# Initialise connection to Reddit API
reddit = praw.Reddit(client_id='', client_secret='',
                     user_agent='Political Leaning')

#Collect every redditors name and return a list of the unique names
df1 = pd.read_csv("C:\\Users\\mikep\\PycharmProjects\\RedditDataCollection\\LabourUK Comments.csv")
df2 = pd.read_csv("C:\\Users\\mikep\\PycharmProjects\\RedditDataCollection\\Tories Comments.csv")
df3 = pd.read_csv("C:\\Users\\mikep\\PycharmProjects\\RedditDataCollection\\UKPolitics Comments.csv")
df4 = pd.concat([df1,df2,df3])

redditor_names = df4["Author"].unique().tolist()
redditor_comment_karma = []
redditor_created_utc = []
redditor_verified_email = []
redditor_is_employee = []
redditor_is_mod = []

count = 0
#Iterate over each name and collect there profile information

for redditor in redditor_names:
    count+=1
    print(str(count), "/", str(len(redditor_names)))

    try:
        reddit_user = reddit.redditor(redditor)

        redditor_comment_karma.append(reddit_user.comment_karma)
        redditor_created_utc.append(reddit_user.created_utc)
        redditor_verified_email.append(reddit_user.has_verified_email)
        redditor_is_employee.append(reddit_user.is_employee)
        redditor_is_mod.append(reddit_user.is_mod)
    except:
        redditor_comment_karma.append("NA")
        redditor_created_utc.append("NA")
        redditor_verified_email.append("NA")
        redditor_is_employee.append("NA")
        redditor_is_mod.append("NA")


dataframe = pd.DataFrame()
dataframe["Redditor"] = redditor_names
dataframe["Total Karma"] = redditor_comment_karma
dataframe["Account Created UTC"] = redditor_created_utc
dataframe["Verified Email"] = redditor_verified_email
dataframe["Employee of Reddit"] = redditor_is_employee
dataframe["Mods a Subreddit"] = redditor_is_mod

dataframe.to_csv("All Unique Redditors.csv")
