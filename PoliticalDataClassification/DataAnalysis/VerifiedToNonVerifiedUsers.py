import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'text.color': "white"})

unique_redditors_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed Unique Redditors.csv")
tories_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed Tories Comments.csv")
labouruk_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed LabourUK Comments.csv")
ukpolitics_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed UKPolitics Comments.csv")

#Sets values that have string "" to Nan values and then drops them
unique_redditors_df["Comment"].replace("", np.nan, inplace=True)
unique_redditors_df["Account Created UTC"].replace("", np.nan, inplace=True)
unique_redditors_df["Verified Email"].replace("", np.nan, inplace=True)
unique_redditors_df["Employee of Reddit"].replace("", np.nan, inplace=True)
unique_redditors_df["Mods a Subreddit"].replace("", np.nan, inplace=True)

unique_redditors_df.dropna(subset=["Comment", "Account Created UTC", "Verified Email", "Employee of Reddit", "Mods a Subreddit"], inplace=True)

#Removes all redditors that have a verified email leaving unverified users only
unique_redditors_df = unique_redditors_df[unique_redditors_df["Verified Email"] == False]

print("Unverified Unique Redditors in r/tories:", len(unique_redditors_df[unique_redditors_df["Redditor"].isin(tories_df["Redditor"])]))
print("Total Unique Users in r/tories:", len(tories_df["Redditor"].unique()))

print("Unverified Unique Redditors in r/labouruk:", len(unique_redditors_df[unique_redditors_df["Redditor"].isin(labouruk_df["Redditor"])]))
print("Total Unique Users in r/labouruk:", len(labouruk_df["Redditor"].unique()))

print("Unverified Unique Redditors in r/ukpolitics:", len(unique_redditors_df[unique_redditors_df["Redditor"].isin(ukpolitics_df["Redditor"])]))
print("Total Unique Users in r/ukpolitics:", len(ukpolitics_df["Redditor"].unique()))

plt.figure()
plt.title("Verified to non verified users in r/tories")
plt.pie([len(unique_redditors_df[unique_redditors_df["Redditor"].isin(tories_df["Redditor"])]), len(tories_df["Redditor"].unique())], labels=["Unverified", "Verified"], colors=["lightseagreen", "purple"], autopct='%1.2f%%')
my_cirle = plt.Circle((0,0), 0.6, color="#202124")
p=plt.gcf()
p.gca().add_artist(my_cirle)
plt.savefig("verified_in_tories.png", transparent=True)

plt.figure()
plt.title("Verified to non verified users in r/labouruk")
plt.pie([len(unique_redditors_df[unique_redditors_df["Redditor"].isin(labouruk_df["Redditor"])]), len(labouruk_df["Redditor"].unique())], labels=["Unverified", "Verified"], colors=["lightseagreen", "purple"], autopct='%1.2f%%')
my_cirle = plt.Circle((0,0), 0.6, color="#202124")
p=plt.gcf()
p.gca().add_artist(my_cirle)
plt.savefig("verified_in_labouruk.png", transparent=True)

plt.figure()
plt.title("Verified to non verified users in r/ukpolitics")
plt.pie([len(unique_redditors_df[unique_redditors_df["Redditor"].isin(ukpolitics_df["Redditor"])]), len(ukpolitics_df["Redditor"].unique())], labels=["Unverified", "Verified"], colors=["lightseagreen", "purple"], autopct='%1.2f%%')
my_cirle = plt.Circle((0,0), 0.6, color="#202124")
p=plt.gcf()
p.gca().add_artist(my_cirle)
plt.savefig("verified_in_ukpolitics.png", transparent=True)

plt.show()