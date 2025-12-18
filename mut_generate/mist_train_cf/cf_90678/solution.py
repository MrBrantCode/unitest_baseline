"""
QUESTION:
Write a function named `longest_substring` that takes a string as input and returns the longest substring containing unique characters. The function should not use any built-in string functions or data structures. The function should iterate over the input string and return the longest substring found. If there are multiple substrings with the same maximum length, any one of them can be returned.
"""

def longest_substring(string):
    longest = ''
    current = ''
    for char in string:
        if char in current:
            if len(current) > len(longest):
                longest = current
            current = char
        else:
            current += char
    if len(current) > len(longest):
        longest = current
    return longest