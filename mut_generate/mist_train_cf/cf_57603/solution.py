"""
QUESTION:
Create a function named `char_count` that takes a string as input and returns a dictionary where the keys are the characters from the string and the values are the number of occurrences of each character. The function should be able to handle strings with spaces and any other characters.
"""

def char_count(string):
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    return result