"""
QUESTION:
Create a function `count_unique_chars` that takes two strings as input and returns the number of unique characters that appear in either string. The function should have a time complexity of O(n), where n is the length of the longer string, and should utilize Python's built-in data structures without using intersection or loops for character comparison.
"""

def count_unique_chars(str1, str2):
    # combine the two strings and convert to set to get unique characters
    unique_chars = set(str1 + str2)
    # return the length of the set
    return len(unique_chars)