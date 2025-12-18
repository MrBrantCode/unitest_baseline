"""
QUESTION:
Construct a function `filter_words_by_vowels` that takes a list of words as input and returns a new list containing only the words with more than three vowels. The function should be case-insensitive when counting vowels.
"""

def filter_words_by_vowels(words):
    return [word for word in words if sum(1 for letter in word if letter.lower() in 'aeiou') > 3]