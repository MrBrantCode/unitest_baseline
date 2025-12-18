"""
QUESTION:
Create a function `filter_words` that uses list comprehension to filter a given list of words and returns a new list containing only the words with a length greater than 10 and no vowels.
"""

def filter_words(words):
    """Filters a list of words and returns a new list containing only the words 
    with a length greater than 10 and no vowels."""
    return [word for word in words if len(word) > 10 and all(letter not in 'aeiou' for letter in word)]