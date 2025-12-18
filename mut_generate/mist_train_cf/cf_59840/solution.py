"""
QUESTION:
Write a function named `can_construct` that takes two parameters: a character sequence (a string) and a collection of words (a list of strings). The function should return `True` if the character sequence can be formed by concatenating any number of words from the collection, and `False` otherwise.
"""

def can_construct(target, wordBank):
    if target == '':
        return True
    for word in wordBank:
        if target.startswith(word) and can_construct(target[len(word):], wordBank):
            return True
    return False