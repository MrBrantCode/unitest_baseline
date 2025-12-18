"""
QUESTION:
Write a function `analyze_sentiment` that takes a sentence as input and returns the sentiment of the sentence as either 'positive', 'negative', or 'neutral'. The function should be able to analyze the sentiment based on the content of the sentence, without relying on any external data or pre-trained models.
"""

def analyze_sentiment(sentence):
    # Initialize sentiment scores
    positive_score = 0
    negative_score = 0

    # Define lists of positive and negative words
    positive_words = ["good", "great", "excellent", "awesome", "love"]
    negative_words = ["bad", "terrible", "awful", "hate"]

    # Convert sentence to lowercase
    sentence = sentence.lower()

    # Split sentence into words
    words = sentence.split()

    # Calculate sentiment scores
    for word in words:
        if word in positive_words:
            positive_score += 1
        elif word in negative_words:
            negative_score += 1

    # Determine sentiment based on scores
    if positive_score > negative_score:
        return 'positive'
    elif positive_score < negative_score:
        return 'negative'
    else:
        return 'neutral'