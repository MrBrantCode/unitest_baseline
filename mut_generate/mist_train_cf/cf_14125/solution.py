"""
QUESTION:
Write a function named count_unique_words that takes a string as input, and returns the number of unique words in the string that do not contain the letter 'a' or have 5 characters or less.
"""

def count_unique_words(text):
    words = text.split()
    unique_words = set(word for word in words if len(word) <= 5 and 'a' not in word)
    return len(unique_words)