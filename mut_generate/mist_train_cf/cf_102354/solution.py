"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in string manipulation functions or methods. The solution should be case-sensitive and have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_string(s):
    reversed_string = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string