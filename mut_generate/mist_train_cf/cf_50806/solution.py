"""
QUESTION:
Create a function `detect_offensive_language` that takes a text string as input and returns `True` if the text contains offensive language and `False` otherwise.
"""

def detect_offensive_language(text):
    # Please note that the actual implementation of this function would involve
    # training a machine learning model or using a natural language processing library
    # to detect offensive language. The following line is a placeholder.
    # For demonstration purposes, we'll use a simple example with a predefined list of offensive words.
    offensive_words = ["bad_word1", "bad_word2"]  # Replace with actual offensive words
    return any(word in text.lower() for word in offensive_words)