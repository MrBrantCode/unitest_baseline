"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input, reverses the order of its alphabetical characters, and returns the resulting string, excluding any non-alphabetical characters. The function should have a time complexity of O(n), where n is the size of the input string.
"""

def reverse_string(s):
    s = ''.join([i for i in s if i.isalpha()])
    return s[::-1]