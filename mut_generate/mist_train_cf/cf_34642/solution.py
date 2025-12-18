"""
QUESTION:
Implement a function `has_repeated_characters` that checks if a given string contains any repeated characters. The function should return `True` if the string contains any repeated characters and `False` otherwise. Do not use any built-in functions or data structures to solve this problem.

The function takes a single string parameter `input_string` and returns a boolean value.
"""

def has_repeated_characters(input_string: str) -> bool:
    matchedSingleCheck = []
    for char in input_string:
        if char in matchedSingleCheck:
            return True
        else:
            matchedSingleCheck.append(char)
    return False