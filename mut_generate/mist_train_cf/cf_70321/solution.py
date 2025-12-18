"""
QUESTION:
Design a function `find_max(words)` that accepts a list of strings `words` and returns a dictionary. The dictionary's key should be the word with the most unique characters from the input list, and its value should be another dictionary containing the frequency of each unique character in that word. If multiple words have the same maximum count of unique characters, return the last one in the list.
"""

def find_max(words):
    max_word = max(words, key=lambda word: len(set(word)), default='')
    char_frequency = {char: max_word.count(char) for char in set(max_word)}
    return {max_word: char_frequency}