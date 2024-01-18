import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tories_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed Tories Comments.csv")
labouruk_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed LabourUK Comments.csv")
ukpolitics_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed UKPolitics Comments.csv")
unique_redditors_df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed Unique Redditors.csv")

#Get each unique redditor who only comments in their chosen subreddit

tories_dropped = pd.Series(tories_df["Redditor"].unique())
tories_dropped = tories_dropped[~tories_dropped.isin(labouruk_df["Redditor"])].dropna()
tories_unique_users = tories_dropped[~tories_dropped.isin(ukpolitics_df["Redditor"])].dropna()

labouruk_dropped = pd.Series(labouruk_df["Redditor"].unique())
labouruk_dropped = labouruk_dropped[~labouruk_dropped.isin(tories_df["Redditor"])].dropna()
labouruk_unique_users = labouruk_dropped[~labouruk_dropped.isin(ukpolitics_df["Redditor"])].dropna()

ukpolitics_dropped = pd.Series(ukpolitics_df["Redditor"].unique())
ukpolitics_dropped = ukpolitics_dropped[~ukpolitics_dropped.isin(labouruk_df["Redditor"])].dropna()
ukpolitics_unique_users = ukpolitics_dropped[~ukpolitics_dropped.isin(tories_df["Redditor"])].dropna()

tories_unique_users = unique_redditors_df[unique_redditors_df["Redditor"].isin(tories_unique_users)].dropna()
labouruk_unique_users = unique_redditors_df[unique_redditors_df["Redditor"].isin(labouruk_unique_users)].dropna()
ukpolitics_unique_users = unique_redditors_df[unique_redditors_df["Redditor"].isin(ukpolitics_unique_users)].dropna()

tories_mean = tories_unique_users["Account Created UTC"].mean()
labouruk_mean = labouruk_unique_users["Account Created UTC"].mean()
ukpolitics_mean = ukpolitics_unique_users["Account Created UTC"].mean()

print(tories_mean)
print(labouruk_mean)
print(ukpolitics_mean)

