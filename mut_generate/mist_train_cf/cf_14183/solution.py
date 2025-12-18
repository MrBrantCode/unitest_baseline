"""
QUESTION:
Create a function called `slice_and_reverse` that takes a string and an integer `n` as parameters. The function should return a reversed substring of the input string, sliced after the nth character from the beginning of the string.
"""

def slice_and_reverse(string, n):
    return string[:n][::-1]