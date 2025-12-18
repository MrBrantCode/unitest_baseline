"""
QUESTION:
Write a function named `contains_plural_words` that takes two parameters: a string `text` and a list of strings `words`. The function should return `True` if the `text` contains all the words from the `words` list in their plural form, and `False` otherwise. The function should handle cases where the words in the list are not already in plural form by appending an 's' to the word to make it plural.
"""

def contains_plural_words(text, words):
    for word in words:
        if word[-1] != 's':  
            word += 's'  
        if word not in text.split():
            return False
    return True