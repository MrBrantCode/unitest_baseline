"""
QUESTION:
Create a function `split_and_filter_words` that takes a string as input, splits it into individual words, and returns a list of words excluding any words that start with a vowel. The function should ignore the case of the first character of each word when checking for vowels.
"""

def split_and_filter_words(s):
    """Splits a string into individual words and returns a list of words excluding any words that start with a vowel."""
    return [word for word in s.split() if not word[0].lower() in 'aeiou']