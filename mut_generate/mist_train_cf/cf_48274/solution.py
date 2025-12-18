"""
QUESTION:
Write a function `remove_duplicates(string1, string2)` that takes two strings as input, removes the common characters between the two strings, and returns the resulting strings with no duplicate characters. The function should return two strings where each string contains unique characters from the original strings, excluding the common characters.
"""

def remove_duplicates(string1, string2):
    common_char = set(string1) & set(string2)
    new_str1 = [char for char in string1 if char not in common_char]
    new_str2 = [char for char in string2 if char not in common_char]
    return "".join(new_str1), "".join(new_str2)