"""
QUESTION:
Write a function `find_word` that takes a sorted list of words and a target word as input, and returns the position of the target word in the list. If the target word is not found, return a message indicating that the word is not in the list. The function should assume that the input list is already sorted.
"""

def find_word(words, target):
    if target in words:
        return words.index(target)
    else:
        return "Word not found in list."