"""
QUESTION:
Write a function `string_length_no_space` that calculates the length of a given string after removing all whitespace characters. The function should manually traverse the string and count the characters without using built-in length functions. It should efficiently handle large input strings and have a time complexity of O(n), where n is the number of characters in the string.
"""

def string_length_no_space(s):
    counter = 0
    for char in s:
        if char != ' ':
            counter += 1
    return counter