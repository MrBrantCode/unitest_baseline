"""
QUESTION:
Write a function `longest_string` that takes a list of strings and an integer `k` as input, and returns the longest string with a length of `k` or less. If multiple strings have the same length, return the lexicographically smallest string among them. If no such string exists, return `None`. The function should have a time complexity of O(n) and should not use any built-in sorting functions.
"""

def longest_string(strings, k):
    longest = None
    for string in strings:
        if len(string) <= k:
            if longest is None or len(string) > len(longest):
                longest = string
            elif len(string) == len(longest):
                if string < longest:
                    longest = string
    return longest