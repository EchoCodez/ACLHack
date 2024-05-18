import gspread as gs

def main():
    gc = gs.service_account(filename='backend/key.json')
    sh1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WkQRziqNg-2dFLd-EDaGIFzWWf8mN6v1lRD9u4JNoWQ/edit?usp=sharing')

    ws1 = sh1.worksheet('Form Responses 1')
    possible = []

    for j in ws1.get_all_records():
        print(j.get("Put the transcript of your conversation here") + ": " + j.get("Upload conversation audio here"))

main()

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import numpy as np

# Define your dataset with fraudulent and good messages
fraudulent_messages = [
    "Let's plan a heist tonight at the bank.",
    "I have a foolproof plan to rob the jewelry store.",
    "Do you know where I can buy illegal firearms?",
    "I need someone to take care of a problem for me.",
    "I know a guy who can get us fake IDs.",
    "Let's meet tonight and discuss our next move.",
    "I have connections with the underworld.",
    "We should eliminate the witness before they talk to the police.",
    "I need to launder some money, do you know anyone who can help?",
    "I have information about a big drug deal going down.",
    "We should deal drugs some day."
]

good_messages = [
    "What a beautiful day!",
    "I'm so excited for the weekend!",
    "Let's go to the beach and have a picnic.",
    "I just got accepted into my dream college!",
    "I love spending time with my friends and family.",
    "Today is going to be a great day!",
    "I'm grateful for all the good things in my life.",
    "Let's spread kindness and positivity wherever we go.",
    "Life is full of amazing opportunities.",
    "I'm feeling so happy and content right now."
]

labels = [1] * len(fraudulent_messages) + [0] * len(good_messages)
sentences = fraudulent_messages + good_messages

# Tokenize the sentences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)
padded_sequences = pad_sequences(sequences, maxlen=100, padding='post', truncating='post')

# Convert labels to a numpy array
labels = np.array(labels)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(word_index) + 1, 64),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
for epoch in range(1, 200):
    print(f"Epoch {epoch}")
    model.fit(X_train, y_train, epochs=1, validation_data=(X_test, y_test), verbose=1)
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"Accuracy: {accuracy}")

# Function to classify a new sentence
def classify_message(message):
    sequence = tokenizer.texts_to_sequences([message])
    padded_sequence = pad_sequences(sequence, maxlen=100, padding='post', truncating='post')
    prediction = model.predict(padded_sequence)
    return 'Fraudulent' if prediction >= 0.5 else 'Good'
