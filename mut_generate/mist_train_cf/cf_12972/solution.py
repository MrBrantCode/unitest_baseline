"""
QUESTION:
Write a function `find_longest_word(dictionary, characters)` that takes a dictionary of words and a set of characters as input and returns the longest word which can be constructed from the given set of characters. The characters in the set can be used multiple times to construct the word. If no word can be constructed, return an empty string. The function should be case-sensitive and the input dictionary can contain duplicate words.
"""

def find_longest_word(dictionary, characters):
    longest_word = ""
    
    for word in dictionary:
        if set(word).issubset(set(characters)):
            if len(word) > len(longest_word):
                longest_word = word
    
    return longest_word