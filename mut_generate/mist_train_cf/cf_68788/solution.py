"""
QUESTION:
Write a function `reverse_sets` that takes a string of digits and an integer `set_count` as input. The function should reverse the string in chunks of `8 * set_count` digits and return the modified string.
"""

def reverse_sets(string, set_count):
    n = 8 * set_count
    return ''.join(string[i:i+n][::-1] for i in range(0, len(string), n))