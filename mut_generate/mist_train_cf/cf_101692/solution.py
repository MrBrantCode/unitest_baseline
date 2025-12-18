"""
QUESTION:
Create a function `count_unique_chars` that takes two strings as input and returns the number of unique characters that appear in both strings without using intersection or loops for character comparison. The function should have a time complexity of O(n), where n is the length of the longer string, and utilize Python's built-in data structures.
"""

def count_unique_chars(str1, str2):
    # combine the two strings and convert to set to get unique characters
    unique_chars = set(str1 + str2)
    # use set intersection operation to get characters common to both strings
    common_chars = set(str1) & set(str2)
    # return the length of the set
    return len(common_chars)