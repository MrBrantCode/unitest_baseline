"""
QUESTION:
Create a function named `filter_words` that takes a list of words as input and returns a new list containing only the words with a length greater than 5.
"""

def filter_words(word_list):
    return [word for word in word_list if len(word) > 5]