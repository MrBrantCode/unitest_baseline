"""
QUESTION:
Create a function called `count_unique_chars` that takes two strings as input and returns the number of unique characters that appear in both strings. The function should not use explicit loops for character comparison, should have a time complexity of O(n) where n is the length of the longer string, and should utilize Python's built-in data structures.
"""

def count_unique_chars(str1, str2):
    # combine the two strings and convert to set to get unique characters
    unique_chars = set(str1 + str2)
    # find the intersection of unique characters in both strings
    common_chars = set(str1).intersection(set(str2))
    # return the length of the intersection
    return len(common_chars)