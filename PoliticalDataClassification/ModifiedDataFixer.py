import pandas as pd

# Read in the dataset for preprocessing
df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\UKPolitics Comments.csv")

# Removes all posts that are deleted
df = df[df["Comment"].str.contains("[deleted]") == True]

# Removes emojis and hyperlinks from each of the comments
df = df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
df["Comment"] = df["Comment"].str.replace(r'http\S+|www.\S+', '', case=False)

# If the comment is less than 30 characters then it is removed from the dataframe
df = df[df["Comment"].str.len() >= 30]

# Dataframe is saved as a new csv
df.to_csv("Cleaned UKPolitics Comments.csv")
