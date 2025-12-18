"""
QUESTION:
Create a Python function named `refine_string` that takes a string as an input and returns a new string where all non-alphanumeric characters are removed.
"""

def refine_string(s):
    for character in s:
        if not character.isalnum():  
            s = s.replace(character, "")  
    return s