"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input and returns the string with all repeating characters removed.
"""

def remove_duplicates(input_str):
    result = []
    for char in input_str:
        if char not in result:
            result.append(char)
    return ''.join(result)