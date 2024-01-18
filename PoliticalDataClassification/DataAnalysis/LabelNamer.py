import pandas as pd

#Simple script that just renames the labels 0 and 1 to their corresponding string label of Left-Wing or Right-Wing
df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Hashed Data\\Hashed UKPolitics Comments.csv")

df["Label"] = df["Label"].astype(str)
df["Label"] = df["Label"].str.replace("0", "Left-Wing")
df["Label"] = df["Label"].str.replace("1", "Right-Wing")

df.to_csv("Hashed UKPolitics Comments.csv")