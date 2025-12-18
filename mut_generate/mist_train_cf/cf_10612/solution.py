"""
QUESTION:
Create a function `sum_ascii_values` that takes a string as input, converts each character to its ASCII value, and returns the sum of all these ASCII values. The function should not take any additional parameters.
"""

def sum_ascii_values(string):
    ascii_sum = 0
    for char in string:
        ascii_sum += ord(char)  # ord() returns the ASCII value of a character
    return ascii_sum