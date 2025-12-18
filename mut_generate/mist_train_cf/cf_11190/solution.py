"""
QUESTION:
Write a function `count_word_occurrences` that takes a string and a list of strings as input, and returns the number of times the string occurs as a whole word in the list, ignoring case sensitivity.
"""

def count_word_occurrences(string, arr):
    count = 0
    for phrase in arr:
        words = phrase.lower().split()
        for word in words:
            if word == string.lower():
                count += 1
    return count