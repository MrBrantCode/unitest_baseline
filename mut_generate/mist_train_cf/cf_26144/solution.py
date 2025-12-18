"""
QUESTION:
Write a function `sentimentClassifier` that takes a sentence as input and classifies its sentiment as either 'positive' or 'negative'.
"""

def sentimentClassifier(sentence):
    if "not" in sentence:
        return 'negative'
    elif "love" in sentence or "great" in sentence:
        return 'positive'
    else:
        return 'negative'