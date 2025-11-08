

#Simple Sentiment Analysis Bot

This is a Python-based Sentiment Analysis project that uses the TextBlob library to analyze and classify the emotional tone (positive, negative, or neutral) of any given text.

It’s a simple console-based application that interacts with the user in real time.


         FEATURES
Analyzes text sentiment in real time

Classifies sentences as Positive, Negative, or Neutral

Displays both sentiment category and polarity score

User-friendly command-line interface

Built using TextBlob — a simple and powerful NLP library

     Technologies Used
     
Python 3.12.10' 

TextBlob (for Natural Language Processing)




SentimentAnalysisProject

│
├── main.py                                   # Entry point of the program

├── sentiment_analyser.py                     # Contains the sentiment analysis logic

└── README.md                                 # Project documentation




⚙️ How It Works

1. The user enters a sentence.

2. The app uses TextBlob to calculate the polarity score (range: -1 to +1).
    >  0: Positive 

     <  0: Negative 

     =  0: Neutral 

 3.The program prints the sentiment and the score in the terminal.









