"""
QUESTION:
Write a function named 'ends_with_s' that takes a list of strings as input and returns a list of strings where the last character of each string is 's'.
"""

def ends_with_s(lst):
    return [string for string in lst if string.endswith('s')]