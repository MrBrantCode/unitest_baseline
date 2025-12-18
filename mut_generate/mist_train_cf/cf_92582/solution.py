"""
QUESTION:
Write a function `find_longest_word(dictionary, characters)` that takes a list of words (`dictionary`) and a string of characters (`characters`) as input, and returns the longest word from the `dictionary` that can be constructed using the characters in `characters`, where each character in `characters` can be used multiple times. If no such word exists, return an empty string.
"""

def find_longest_word(dictionary, characters):
    longest_word = ""
    
    for word in dictionary:
        if set(word).issubset(set(characters)):
            if len(word) > len(longest_word):
                longest_word = word
    
    return longest_word