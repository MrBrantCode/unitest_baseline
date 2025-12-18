"""
QUESTION:
Write a function `longest_string(strings, k)` that takes a list of strings `strings` and an integer `k` as input, and returns the longest string in `strings` with length of `k` or less. If multiple strings have the same length, return the lexicographically smallest string among them. The function should have a time complexity of O(n), where n is the number of strings in `strings`, and should not use any built-in sorting functions.
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