"""
QUESTION:
Write a function named `lookup_index` that takes in a list of words and a target word, and returns the index of the target word in the list. If the target word does not exist in the list, return -1. The function should have a time complexity of O(n), where n is the length of the list. The list of words will not be empty, may contain duplicates, and the target word will always be a string.
"""

def lookup_index(words, target):
    for index, word in enumerate(words):
        if word == target:
            return index
    return -1