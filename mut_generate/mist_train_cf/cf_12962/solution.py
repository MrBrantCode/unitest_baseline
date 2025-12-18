"""
QUESTION:
Create a function `filter_words` that takes a string as input and returns a list of words. The function should split the input string into words by any number of whitespace characters, remove any empty strings, and exclude words with less than two characters.
"""

def filter_words(s):
    return [word for word in s.split() if len(word) >= 2]