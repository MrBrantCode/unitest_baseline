"""
QUESTION:
Write a function `filter_words` that takes a list of words as input and returns a new list containing only the words that have a length of more than 10 characters and do not contain any vowels. The vowels are 'a', 'e', 'i', 'o', 'u'.
"""

def filter_words(words):
    """Return a new list containing only the words that have a length of more than 10 characters and do not contain any vowels."""
    vowels = 'aeiou'
    return [word for word in words if len(word) > 10 and all(letter not in vowels for letter in word)]