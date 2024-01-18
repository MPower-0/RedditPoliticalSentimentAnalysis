import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = 11, 5

tories_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed Tories Comments.csv")
labouruk_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed LabourUK Comments.csv")

#Get the users who post in both subreddits the most
#Get their average karma on their comments in both subreddits and compare to others

tories_unique = pd.Series(tories_df["Redditor"].unique())
labouruk_unique = pd.Series(labouruk_df["Redditor"].unique())

tories_in_labouruk = (tories_unique.isin(labouruk_unique))

#Creates and returns a dataframe containing unique names that appear in both dataframes
unique_in_both = pd.DataFrame()
unique_in_both["Redditor"] = tories_unique
unique_in_both["Both"] = tories_in_labouruk
unique_in_both = unique_in_both[unique_in_both["Both"]]

#Return the count of all comments that each unique user has
tories_df_dropped = tories_df[tories_df["Redditor"].isin(unique_in_both["Redditor"])].dropna()
tories_value_counts = tories_df_dropped["Redditor"].value_counts()

labouruk_df_dropped = labouruk_df[labouruk_df["Redditor"].isin(unique_in_both["Redditor"])].dropna()
labouruk_value_counts = labouruk_df_dropped["Redditor"].value_counts()

tories_counts_df = tories_value_counts.to_frame().reset_index()
tories_counts_df = tories_counts_df.rename(columns={"Redditor": "Count", "index":"Redditor"})

labouruk_counts_df = labouruk_value_counts.to_frame().reset_index()
labouruk_counts_df = labouruk_counts_df.rename(columns={"Redditor": "Count", "index":"Redditor"})


combined_count = (tories_counts_df.merge(labouruk_counts_df, on="Redditor"))
combined_count = combined_count.sort_values(["Count_x", "Count_y"], ascending=[False, False])

#Outputs the file as a csv so that the values can be manually compared
combined_count.to_csv("Comment Count.csv")

#Manually selected users after deciding on users who had more than 50 comments in both subreddits and a similar amount in both subreddits
users_to_analyse = ["b0cc008d4a8fbced52183219ef5fa635511090d9c4cc653a5192553ee2287762","2caf414cb95e3dadd07b9da56fdd51d6793fdaf97b6a7bbbe9ac01093baceb39",
                  "26cf9a8e8d088a3ec5d175f916003d1fcbb06f969c7abc6cd73a208cb120454f", "95e215f5a8e499f2bdb3432c5c39f0c3585b073b166b45b78d1465bfe5583a62", "e37f12987aa58f5a69d81e2252832510dad0eb901087e4d82d9f89f46813ad83"]

user1_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[0]]
user1_labouruk = labouruk_df.loc[labouruk_df["Redditor"] == users_to_analyse[0]]

user2_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[1]]
user2_labouruk = labouruk_df.loc[labouruk_df["Redditor"] == users_to_analyse[1]]

user3_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[2]]
user3_labouruk = labouruk_df.loc[labouruk_df["Redditor"] == users_to_analyse[2]]

user4_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[3]]
user4_labouruk = labouruk_df.loc[labouruk_df["Redditor"] == users_to_analyse[3]]

user5_tories = tories_df.loc[tories_df["Redditor"] == users_to_analyse[4]]
user5_labouruk = labouruk_df.loc[labouruk_df["Redditor"] == users_to_analyse[4]]

user1_data = [user1_tories["Comment Karma"], user1_labouruk["Comment Karma"]]
user2_data = [user2_tories["Comment Karma"], user2_labouruk["Comment Karma"]]
user3_data = [user3_tories["Comment Karma"], user3_labouruk["Comment Karma"]]
user4_data = [user4_tories["Comment Karma"], user4_labouruk["Comment Karma"]]
user5_data = [user5_tories["Comment Karma"], user5_labouruk["Comment Karma"]]

#Create boxplots of all the data on each user
plt.figure()
plt.title("User 1")
plt.boxplot(user1_data, vert=0)
plt.yticks([1, 2], ["User 1 r/tories", "User 1 r/labouruk"])

plt.savefig("user1_karma_boxplot", transparent=True)

plt.figure()
plt.title("User 2")
plt.boxplot(user2_data, vert=0)
plt.yticks([1, 2], ["User 2 r/tories", "User 2 r/labouruk"])

plt.savefig("user2_karma_boxplot", transparent=True)

plt.figure()
plt.title("User 3")
plt.boxplot(user3_data, vert=0)
plt.yticks([1, 2], ["User 3 r/tories", "User 3 r/labouruk"])

plt.savefig("user3_karma_boxplot", transparent=True)

plt.figure()
plt.title("User 4")
plt.boxplot(user4_data, vert=0)
plt.yticks([1, 2], ["User 4 r/tories", "User 4 r/labouruk"])

plt.savefig("user4_karma_boxplot", transparent=True)

plt.figure()
plt.title("User 5")
plt.boxplot(user5_data, vert=0)
plt.yticks([1, 2], ["User 5 r/tories", "User 5 r/labouruk"])

plt.savefig("user5_karma_boxplot", transparent=True)

plt.show()