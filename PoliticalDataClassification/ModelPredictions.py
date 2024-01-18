import pandas as pd
from tensorflow.keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

# Read in the csv of cleaned data
prediction_ds = pd.read_csv(
    "C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Complete Reddit Data\\Cleaned Data\\Cleaned UKPolitics Comments.csv")
pred_x = prediction_ds["Comment"]

# Load in the trained ML model
model = load_model(
    "C:\\Users\\mikep\\Documents\\University\\Final Year Project\\Saved Models\\CNN Text Classification Model.h5")

# Preprocess the data so that it can be fed into the model
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(pred_x)
pred_x = tokenizer.texts_to_sequences(pred_x)

maxlen = 750
pred_x = pad_sequences(pred_x, padding="post", maxlen=maxlen)

# Make predictions on the data and add it to a new column
predictions = (model.predict(pred_x) > 0.5).astype("int32")
predictions = predictions.flatten()

prediction_ds["Label"] = pd.Series(predictions)
prediction_ds.to_csv("Labelled Cleaned UKPolitics Comments.csv")
