import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
from sklearn.model_selection import train_test_split


raw_train_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Cleaned Karma Based Naively Labelled Dataset.csv")
test_ds = pd.read_csv("C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Training and Testing Data\\Political Comments Labelled.csv")

train_x = raw_train_ds["Comments"]
train_y = raw_train_ds["Label"]

test_x = test_ds["Comments"]
test_y = test_ds["Label"]

train_x, val_x, train_y, val_y = train_test_split(train_x, train_y, stratify=train_y, random_state=48, test_size=0.1)

bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-4_H-256_A-4/2")

text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
preprocessed_text = bert_preprocess(text_input)
outputs = bert_encoder(preprocessed_text)
l = tf.keras.layers.Dropout(0.1, name="dropout")(outputs['pooled_output'])
l = tf.keras.layers.Dense(1, activation='sigmoid', name="output")(l)
model = tf.keras.Model(inputs=[text_input], outputs = [l])

optimizer = tf.keras.optimizers.experimental.Adam(learning_rate=0.001)
model.compile(optimizer=optimizer,
 loss='binary_crossentropy',
 metrics=["accuracy"])

model.fit(train_x, train_y, batch_size=32, epochs=50, validation_data=(val_x, val_y))

test_loss, test_acc = model.evaluate(test_x, test_y, verbose=2)
print("Test Accuracy:", test_acc)
print("Test Loss", test_loss)