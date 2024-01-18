import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras import layers

from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

# CSV are read into dataframes
raw_train_ds = pd.read_csv(
    "C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Cleaned Karma Based Naively Labelled Dataset.csv")
test_ds = pd.read_csv(
    "C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Political Comments Labelled.csv")

# Data is split into training and validation data sets
train_x = raw_train_ds["Comments"]
train_y = raw_train_ds["Label"]

test_x = test_ds["Comments"]
test_y = test_ds["Label"]

train_x, val_x, train_y, val_y = train_test_split(train_x, train_y, stratify=train_y, random_state=48, test_size=0.2)

# Data sets are tokenised and padded before passing through the model
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(train_x)

train_x = tokenizer.texts_to_sequences(train_x)
val_x = tokenizer.texts_to_sequences(val_x)
test_x = tokenizer.texts_to_sequences(test_x)

vocab_size = len(tokenizer.word_index) + 1

maxlen = 750

train_x = pad_sequences(train_x, padding="post", maxlen=maxlen)
val_x = pad_sequences(val_x, padding="post", maxlen=maxlen)
test_x = pad_sequences(test_x, padding="post", maxlen=maxlen)

embedding_dim = 50

# The model is a simple CNN model with only a couple of layers
input_dim = train_x.shape[1]
model = Sequential()
model.add(layers.Embedding(input_dim=vocab_size,
                           output_dim=embedding_dim,
                           input_length=maxlen))

model.add(layers.Conv1D(32, 3, padding="same", activation="relu"))
model.add(layers.MaxPooling1D())
model.add(layers.Flatten())
model.add(layers.Dense(256, activation="relu"))

model.add(layers.Dense(1, activation="sigmoid"))

# Optimiser uses Adam and binary crossentropy to label
optimizer = tf.keras.optimizers.experimental.Adam(learning_rate=0.001)
model.compile(loss="binary_crossentropy",
              optimizer=optimizer,
              metrics=["accuracy"])

# Model is fitted on the training dataset over 5 epochs
model.fit(train_x, train_y, epochs=5, validation_data=(val_x, val_y), batch_size=32)

# Training, validation and test accuracy is output
test_loss, test_acc = model.evaluate(test_x, test_y, verbose=2)
print("Test Accuracy:", test_acc)
print("Test Loss", test_loss)

# Model is saved
model.save("CNN Text Classification Model.h5")
