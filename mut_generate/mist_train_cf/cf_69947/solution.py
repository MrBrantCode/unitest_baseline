"""
QUESTION:
Create a function `is_string_happy` that determines whether a given string is "happy". A string is considered happy if it meets two conditions: 
1) it does not contain any digits, and 
2) all its characters are the same.
"""

def is_string_happy(string):
    if any(char.isdigit() for char in string):
        return False
    return all(string[i] == string[0] for i in range(1, len(string)))