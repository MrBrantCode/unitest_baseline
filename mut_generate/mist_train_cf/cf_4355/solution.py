"""
QUESTION:
Write a function `classify_sentiment(text)` to classify the sentiment of a given text as positive, negative, or neutral. The function should use a custom sentiment analysis algorithm that assigns higher scores to words with stronger emotional intensity and lower scores to words with weaker emotional intensity. The function should take a string `text` as input and return a string indicating the sentiment of the text.
"""

def classify_sentiment(text):
    # Custom sentiment analysis algorithm to assign scores to words
    sentiment_scores = {
        'exceeded': 0.9,
        'expectations': 0.6,
        'happier': 0.8,
        'happy': 0.7,
        "couldn't": -0.6
        # Add more words and their corresponding scores as needed
    }

    # Preprocess the text by removing punctuation and converting to lowercase
    processed_text = text.lower().replace('.', '').replace('!', '').replace('?', '')

    # Split the text into individual words
    words = processed_text.split()

    # Calculate the sentiment score for the entire text
    total_score = sum(sentiment_scores.get(word, 0) for word in words)

    # Classify the sentiment based on the score
    if total_score > 0:
        sentiment = 'Positive'
    elif total_score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment