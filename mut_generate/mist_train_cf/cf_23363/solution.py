"""
QUESTION:
Create a function named `capitalize` that takes a string as input and returns a new string where each character is capitalized.
"""

def capitalize(string):
    new_string = ""
    for c in string:
        new_string += c.upper()
    return new_string