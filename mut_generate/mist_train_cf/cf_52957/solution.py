"""
QUESTION:
Write a function `isolate_unique_character(words, target)` that takes a list of words and a target word as input, and returns a list of unique alphabetical characters from the target word. The function should maintain the order of characters as they appear in the original word and ignore the case where the target word is not found in the list.
"""

def isolate_unique_character(words, target):
    for word in words:
        if word == target:
            return list(dict.fromkeys(word))