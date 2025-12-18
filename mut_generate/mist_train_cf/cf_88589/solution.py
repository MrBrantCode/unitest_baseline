"""
QUESTION:
Create a function named `reverse_string` that takes a string and a number `n` as inputs. The function should return a string containing the first `n` characters of the input string in reverse order, handling alphanumeric characters, special characters, punctuation marks, whitespace, and non-alphanumeric characters. If the input string's length is less than `n`, return the reversed string.
"""

def reverse_string(s, n):
    return s[:n][::-1]