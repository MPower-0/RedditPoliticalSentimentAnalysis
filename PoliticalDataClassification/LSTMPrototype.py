import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Sequential

from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense
from keras.optimizers import Adam

#raw_train_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Training.csv")
raw_train_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Cleaned Larger Naively Labelled Political Comments and their Leaning.csv")
test_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Political Comments Labelled.csv")

train_x = raw_train_ds["Comments"]
train_y = raw_train_ds["Label"]

test_x = test_ds["Comments"]
test_y = test_ds["Label"]

from collections import Counter
def counter_word(text):
    count = Counter()
    for i in text.values:
        for word in i.split():
            count[word] += 1
    return count

counter = counter_word(train_x)


num_words = len(counter)
max_length = 100

train_x, val_x, train_y, val_y = train_test_split(train_x, train_y, stratify=train_y, random_state=48, test_size=0.1)

tokenizer = Tokenizer(num_words=num_words)
tokenizer.fit_on_texts(train_x)

train_sequences = tokenizer.texts_to_sequences(train_x)

train_padded = pad_sequences(train_sequences, maxlen=max_length, padding="post", truncating="post")

val_sequences = tokenizer.texts_to_sequences(val_x)
val_padded = pad_sequences(val_sequences, maxlen=max_length, padding="post", truncating="post")

test_sequences = tokenizer.texts_to_sequences(test_x)
test_padded = pad_sequences(test_sequences, maxlen=max_length, padding="post", truncating="post")

model = Sequential()
model.add(Embedding(num_words, 32, input_length=max_length))
model.add(LSTM(64, dropout=0.1))
model.add(Dense(1, activation="sigmoid"))

optimizer = Adam(learning_rate = 0.001)
model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])

model.fit(train_padded, train_y, epochs=50, validation_data=(val_padded, val_y), batch_size=32)

test_loss, test_acc = model.evaluate(test_padded, test_y, verbose=2)
print("Test Accuracy:", test_acc)
print("Test Loss", test_loss)