"""
QUESTION:
Create a function `filter_words` that takes a list of words as input and returns a new list containing only the words that have at least one vowel, maintaining the original order. A word with multiple vowels is considered as having one vowel occurrence.
"""

def filter_words(words):
    vowels = set('aeiou')
    return [word for word in words if any(char.lower() in vowels for char in word)]