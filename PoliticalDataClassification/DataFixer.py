import pandas as pd

# Read in the training dataset and the testing manually labelled dataset
df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Karma Based Naively Labelled Dataset.csv")
df2 = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Political Comments Labelled.csv")

# Removes all rows from the training dataset that are in the testing dataset
cond = df["Comments"].isin(df2['Comments'])
df.drop(df[cond].index, inplace=True)

# Removes all posts that are deleted
df = df[df["Comments"].str.contains("[deleted]") == True]

# Removes emojis and hyperlinks from each of the comments
df = df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
df["Comments"] = df["Comments"].str.replace(r'http\S+|www.\S+', '', case=False)

# If the comment is less than 30 characters then it is removed from the dataframe
df = df[df["Comments"].str.len() >= 30]

#Removes comments that have less than 5 karma
df["Comment Karma"] = df["Comment Karma"].astype(int)
df = df[df["Comment Karma"] > 4]

# Checks if one class is over-represented and down-samples the dataset if that's the case so the classes are the same size
if ((df["Label"].value_counts())[0] > (df["Label"].value_counts())[1]):
    df_left = df[df["Label"] == "0"]
    df_right = df[df["Label"] == "1"]
    df_left_downsampled = df_left.sample(df_right.shape[0])
    df = pd.concat([df_left_downsampled, df_right])
else:
    df_left = df[df["Label"] == "0"]
    df_right = df[df["Label"] == "1"]
    df_right_downsampled = df_right.sample(df_left.shape[0])
    df = pd.concat([df_right_downsampled, df_left])

# Dataframe is saved as a new csv
df.to_csv("Cleaned Karma Based Naively Labelled Dataset.csv")
