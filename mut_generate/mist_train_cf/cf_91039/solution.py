"""
QUESTION:
Implement a function `calculate_length` that takes a string as input and returns its length without using the built-in `len()` function. The function should be able to handle strings of any length and complexity, including special characters, numbers, and whitespace.
"""

def calculate_length(string):
    count = 0
    for _ in string:
        count += 1
    return count