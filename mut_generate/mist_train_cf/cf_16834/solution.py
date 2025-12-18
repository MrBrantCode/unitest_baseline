"""
QUESTION:
Write a function `calculate_length` that calculates the length of a given string without using any built-in string length functions or methods. The function should take one parameter, the input string, and return the length of the string as an integer.
"""

def calculate_length(string):
    count = 0
    for _ in string:
        count += 1
    return count