"""
QUESTION:
Create a function named `check_string_case` that takes a list of strings as input and returns the index of the first string that contains both uppercase and lowercase letters. If no such string is found, return -1. The function should iterate through the list only until it finds a string that meets the condition.
"""

def check_string_case(strings):
    for i, string in enumerate(strings):
        if any(char.isupper() for char in string) and any(char.islower() for char in string):
            return i
    return -1