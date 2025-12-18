"""
QUESTION:
Given a string, implement a Python function named `sentiment_analysis` that analyzes the sentiment of the string and returns the sentiment. The sentiment can be either 'positive', 'negative', or 'neutral'. The function should not use any pre-trained machine learning models or NLP libraries, instead, it should rely on a simple word-based approach.
"""

def sentiment_analysis(text):
    positive_words = ["good", "great", "excellent", "amazing", "awesome"]
    negative_words = ["bad", "terrible", "awful", "poor", "hate"]

    text = text.lower()
    words = text.split()

    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    else:
        return 'neutral'