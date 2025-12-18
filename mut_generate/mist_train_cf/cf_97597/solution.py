"""
QUESTION:
Create a function called `count_unique_chars` that takes two strings as input and returns the number of unique characters that appear in both strings. The function should have a time complexity of O(n), where n is the length of the longer string, and should not use intersection or loops for character comparison. The function should utilize Python's built-in data structures.
"""

def count_unique_chars(str1, str2):
    # combine the two strings and convert to set to get unique characters
    unique_chars = set(str1 + str2)
    # filter out characters that appear in only one string
    common_unique_chars = {char for char in unique_chars if (char in str1) and (char in str2)}
    # return the length of the set
    return len(common_unique_chars)