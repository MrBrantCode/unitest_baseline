"""
QUESTION:
Write a function `calculate_length` that calculates the length of a given string without using any built-in string length functions or methods. The function should have a time complexity of O(n), where n is the length of the string.
"""

def calculate_length(string):
    count = 0
    for char in string:
        count += 1
    return count