import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

#raw_train_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Training.csv")
##test_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Testing.csv")
test_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Political Comments Labelled.csv")
raw_train_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Cleaned Karma Based Naively Labelled Dataset.csv")

train_x = raw_train_ds["Comments"]
train_y = raw_train_ds["Label"]

test_x = test_ds["Comments"]
test_y = test_ds["Label"]

train_x, val_x, train_y, val_y = train_test_split(train_x, train_y, stratify=train_y, random_state=48, test_size=0.1)

vectorizer = CountVectorizer()
vectorizer.fit(train_x)

train_x = vectorizer.transform(train_x)
val_x = vectorizer.transform(val_x)
test_x = vectorizer.transform(test_x)

classifier = LogisticRegression(max_iter=1000)
classifier.fit(train_x, train_y)

val_score = classifier.score(val_x, val_y)
print("Val: ", val_score)

test_score = classifier.score(test_x, test_y)
print("Test: ", test_score)