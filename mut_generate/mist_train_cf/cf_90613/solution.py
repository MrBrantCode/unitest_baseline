"""
QUESTION:
Create a function called `classify_sentence` that takes a string sentence as input and returns a string indicating whether the sentiment of the sentence is 'positive', 'negative', or 'neutral'. The function should use two predefined lists of positive and negative words to calculate the sentiment score, and classify the sentence based on the following thresholds: if the sentiment score is greater than 1.0, classify as 'positive'; if less than -1.0, classify as 'negative'; otherwise, classify as 'neutral'. The function should ignore common stopwords like 'a', 'an', 'the', 'and', etc., and consider the sentiment of each word in a case-insensitive manner.
"""

import re

positive_words = ['good', 'great', 'excellent', 'happy']
negative_words = ['bad', 'terrible', 'awful', 'sad']
stopwords = ['a', 'an', 'the', 'and', 'to', 'is']
positive_threshold = 1.0
negative_threshold = -1.0

def classify_sentence(sentence):
    tokenized_sentence = re.findall(r'\b\w+\b', sentence.lower())
    filtered_sentence = [word for word in tokenized_sentence if word not in stopwords]
    sentiment_score = sum(1 for word in filtered_sentence if word in positive_words) - sum(1 for word in filtered_sentence if word in negative_words)
    if sentiment_score > positive_threshold:
        return 'positive'
    elif sentiment_score < negative_threshold:
        return 'negative'
    else:
        return 'neutral'