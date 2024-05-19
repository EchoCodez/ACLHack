import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import numpy as np

fraudulent_messages = [
    "I am going to rob a bank", "Let's smuggle drugs across the border", "I will murder my enemy",
    "Breaking and entering is easy", "I'm going to commit insurance fraud", "Let's start a Ponzi scheme",
    "I will engage in identity theft", "Let's kidnap someone for ransom", "I am going to hack into a government database",
    "Let's engage in money laundering", "I will commit perjury in court", "Let's vandalize public property",
    "I am going to engage in human trafficking", "Let's commit arson for insurance money", "I will engage in cyberbullying",
    "Let's steal cars for profit", "I am going to distribute illegal substances", "Let's commit copyright infringement",
    "I will engage in embezzlement", "Let's engage in insider trading", "I am going to commit tax evasion",
    "Let's engage in illegal gambling", "I will engage in securities fraud", "Let's engage in blackmail",
    "I am going to engage in counterfeiting", "Let's commit assault and battery", "I will engage in extortion",
    "Let's engage in drug trafficking", "I am going to engage in public corruption", "Let's engage in animal cruelty",
    "I will engage in stalking", "Let's engage in espionage", "I am going to engage in money counterfeiting",
    "Let's engage in bribery", "I will engage in human rights abuses", "Let's engage in environmental crimes",
    "I am going to engage in arms trafficking", "Let's engage in hate crimes", "I will engage in intellectual property theft",
    "Let's engage in child pornography", "I am going to engage in cyberstalking", "Let's engage in white-collar crimes",
    "I will engage in drug manufacturing", "Let's engage in wire fraud", "I am going to engage in credit card fraud",
    "Let's engage in mail fraud", "I will engage in computer crimes", "Let's engage in identity fraud",
    "I am going to engage in money counterfeiting", "Let's engage in healthcare fraud", "I will engage in tax fraud",
    "Let's engage in bribery", "I am going to engage in mortgage fraud", "Let's engage in public corruption",
    "I will engage in election crimes", "Let's engage in voting fraud", "I am going to engage in police misconduct",
    "Let's engage in witness tampering", "I will engage in perjury", "Let's engage in jury tampering",
    "I am going to engage in obstruction of justice", "Let's engage in contempt of court", "I will engage in racketeering",
    "Let's engage in price fixing", "I am going to engage in antitrust violations", "Let's engage in monopolization",
    "I will engage in consumer fraud", "Let's engage in securities fraud", "I am going to engage in accounting fraud",
    "Let's engage in financial fraud", "I will engage in wire fraud", "Let's engage in mail fraud",
    "I am going to engage in tax evasion", "Let's engage in money laundering", "I will engage in embezzlement",
    "Let's engage in bribery", "I am going to engage in extortion", "Let's engage in blackmail", "I will engage in corruption",
    "Let's engage in influence peddling", "I am going to engage in kickbacks", "Let's engage in graft", "I will engage in nepotism",
    "Let's engage in cronyism", "I am going to engage in favoritism", "Let's engage in patronage", "I will engage in vote-buying",
    "Let's engage in electoral fraud", "I am going to engage in tampering", "Let's engage in sabotage", "I will engage in espionage",
    "Let's engage in treason", "I am going to engage in sedition", "Let's engage in rebellion", "I will engage in terrorism",
    "Let's engage in piracy", "I am going to engage in war crimes", "Let's engage in genocide", "I will engage in crimes against humanity",
    "Let's engage in ethnic cleansing", "I am going to engage in aggression", "Let's engage in torture"
]

good_messages = [
    "Good morning!", "How are you today?", "What's for lunch?", "Have a nice day!", "Did you watch the game last night?",
    "I'm looking forward to the weekend.", "The weather is nice today.", "I'm feeling excited about the upcoming trip.",
    "Let's meet for coffee sometime.", "I'm thinking of redecorating my room.", "Have you read any good books lately?",
    "I'm excited to try that new restaurant.", "Do you want to go for a walk?", "I had a great time at the party last night.",
    "I need to buy some groceries later.", "I'm planning to visit my parents next weekend.", "What are your plans for the holidays?",
    "I'm feeling motivated to start a new project.", "Let's go see a movie together.", "I'm enjoying this conversation.",
    "Do you have any pets?", "I'm feeling grateful for the little things in life.", "Let's plan a picnic for next weekend.",
    "I'm looking forward to seeing my friends.", "Do you want to grab dinner together?", "I'm excited to try out that new recipe.",
    "Let's go for a hike this weekend.", "I'm feeling inspired to learn something new.", "What's your favorite movie?",
    "I'm enjoying the sunshine today.", "Let'sa go shopping for some new clothes.", "I'm feeling relaxed after a long day.",
    "Do you have any plans for the evening?", "I'm looking forward to reading a book tonight.", "Let's go for a bike ride.",
    "I'm excited about the upcoming holiday season.", "What's your favorite hobby?", "I'm feeling optimistic about the future.",
    "Let's go for a swim at the beach.", "I'm enjoying listening to music right now.", "Do you want to play a board game?",
    "I'm feeling content with life.", "Let's have a barbecue this weekend.", "I'm excited about the possibilities ahead.",
    "What's your favorite food?", "I'm feeling proud of my accomplishments.", "Let's plan a weekend getaway.",
    "I'm looking forward to the new season of my favorite TV show.", "Do you want to go for a run?", "I'm feeling curious about the world.",
    "Let's have a movie night at home.", "I'm excited to try out a new restaurant.", "What's your favorite book?",
    "I'm feeling grateful for my friends and family.", "Let's go to a concert together.", "I'm looking forward to spending time outdoors.",
    "Do you want to go camping?", "I'm feeling excited about the future.", "Let's have a game night with friends.",
    "I'm excited to start a new chapter in my life.", "What's your favorite place to travel?", "I'm feeling happy and content.",
    "Let's have a picnic in the park.", "I'm looking forward to the weekend ahead.", "Do you want to go for a drive?",
    "I'm feeling relaxed and at ease.", "Let's go to the beach this weekend.", "I'm excited to try something new.",
    "What's your favorite TV show?", "I'm feeling inspired by nature.", "Let's have a potluck dinner with friends.",
    "I'm looking forward to spending time with loved ones.", "Do you want to go for a hike in the mountains?",
    "I'm feeling grateful for the little moments in life.", "Let's have a movie marathon.", "I'm excited to explore new places.",
    "What's your favorite sport?", "I'm feeling optimistic about the future.", "Let's have a barbecue in the backyard.",
    "I'm looking forward to trying new recipes."
]

labels = [1] * len(fraudulent_messages) + [0] * len(good_messages)
sentences = fraudulent_messages + good_messages

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)
padded_sequences = pad_sequences(sequences, maxlen=100, padding='post', truncating='post')

labels = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(word_index) + 1, 64),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

for epoch in range(1, 200):
    print(f"Epoch {epoch}")
    model.fit(X_train, y_train, epochs=1, validation_data=(X_test, y_test), verbose=1)
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"Accuracy: {accuracy}")

def classify_message(message):
    sequence = tokenizer.texts_to_sequences([message])
    padded_sequence = pad_sequences(sequence, maxlen=100, padding='post', truncating='post')
    prediction = model.predict(padded_sequence)
    return 'Fraudulent' if prediction >= 0.5 else 'Good'

