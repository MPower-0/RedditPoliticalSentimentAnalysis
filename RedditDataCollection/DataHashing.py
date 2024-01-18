import hashlib
import pandas as pd

#Reads in a dataframe hashes the data using sha256 and outputs the new csv file
df = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\All Unique Redditors.csv")

df["Redditor"] = df["Redditor"].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())

df.to_csv("Hashed Unique Redditors.csv")
