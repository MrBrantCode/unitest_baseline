"""
QUESTION:
Write a function `calculate_length` that calculates the length of a given string without using the built-in length function. The function should iterate through each character of the string and count them. It should handle non-empty strings and return the total count. The input will be a string, and the output should be an integer representing the string's length.
"""

def calculate_length(string):
    count = 0
    for char in string:
        count += 1
    return count