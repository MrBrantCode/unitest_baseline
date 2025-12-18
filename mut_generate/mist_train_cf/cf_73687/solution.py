"""
QUESTION:
Write a function called `equal_letter_words` that takes a list of strings as input. The function should return a list of words where each word is either made up of the same letter or has each of its letters appearing an equal number of times, regardless of case. If no such words exist, return an empty list.
"""

from collections import Counter

def equal_letter_words(words):
    result = []
    for word in words:
        letter_counts = Counter(word.lower())  # Count each letter in the word regardless of case
        if len(set(letter_counts.values())) == 1:  # Check if all letters occur the same number of times
            result.append(word)
    return result