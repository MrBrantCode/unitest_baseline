"""
QUESTION:
Create a function `get_last_n_chars` that takes a string and an integer `n` as input and returns a string with the last `n` characters of the given string. If `n` is greater than or equal to the length of the string, the function should return the original string without any truncation. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def get_last_n_chars(string, n):
    return string[-n:] if n < len(string) else string