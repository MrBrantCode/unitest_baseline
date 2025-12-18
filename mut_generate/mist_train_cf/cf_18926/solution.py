"""
QUESTION:
Write a function called `longest_string` that takes a list of strings and an integer `k` as input. The function should return the longest string with a length of `k` or less. In cases where multiple strings have the same maximum length, return the lexicographically smallest one. The function should achieve this in a time complexity of O(n) without using any built-in sorting functions.
"""

def longest_string(strings, k):
    max_length = -1
    smallest_lex = ""
    
    for string in strings:
        if len(string) <= k:
            if len(string) > max_length:
                max_length = len(string)
                smallest_lex = string
            elif len(string) == max_length and string < smallest_lex:
                smallest_lex = string
    
    return smallest_lex