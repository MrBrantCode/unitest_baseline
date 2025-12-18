"""
QUESTION:
Write a function called `reverse_words` that takes a string as input and returns a string containing the words in the input string in reverse order, while preserving the order of characters within each word.
"""

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split())