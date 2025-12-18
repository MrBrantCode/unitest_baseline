"""
QUESTION:
Write a function called `compute_string_length` that takes a string `s` as input and returns the length of the string without using the built-in `len()` function, loops, recursion, or any string manipulation functions.
"""

def compute_string_length(s):
    characters = list(s)
    count = 0
    try:
        while True:
            characters[count]
            count += 1
    except IndexError:
        return count