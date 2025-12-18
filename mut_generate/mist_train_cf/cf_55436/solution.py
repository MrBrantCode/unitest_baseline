"""
QUESTION:
Write a function named "substrings" that takes a string as input and returns the total count of substrings, including single characters and combinations of characters, that can be formed from the input string. The function should not take into account the actual substrings themselves, only the count.
"""

def substrings(string):
    length = len(string)
    return (length * (length + 1)) // 2