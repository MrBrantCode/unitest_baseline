"""
QUESTION:
Write a function called `find_longest_string` that takes a list of strings as a parameter. The function should return the longest string from the list that meets the following conditions: the string has at least 3 characters and contains only alphabetic characters. The function should return the longest string in uppercase.
"""

def find_longest_string(strings):
    longest = max((s for s in strings if s.isalpha() and len(s) >= 3), key=len, default='')
    return longest.upper()