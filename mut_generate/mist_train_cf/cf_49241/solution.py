"""
QUESTION:
Create a function `find_words(word_list, character_set)` that takes a list of words and a set of characters as input, and returns a new list containing only the words that include all characters from the specified set.
"""

def find_words(word_list, character_set):
    return [word for word in word_list if all(char in word for char in character_set)]