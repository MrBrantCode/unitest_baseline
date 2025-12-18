"""
QUESTION:
Create a function called `remove_letters(word)` that takes a string `word` as input and returns a new string containing only the first letter of the input word. If the input word has a length of 1, return the word itself.
"""

def remove_letters(word):
    if len(word) > 1:
        return word[0]
    else:
        return word