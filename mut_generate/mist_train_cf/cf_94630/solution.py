"""
QUESTION:
Create a function `create_new_string(original_string)` that takes an input string `original_string`. The function should return a new string containing all uppercase letters from `original_string`, provided that the new string's length is greater than 5 and it contains at least one special character. If such a string cannot be created, return "No such string exists."
"""

import string

def create_new_string(original_string):
    new_string = "".join([char for char in original_string if char.isupper()])
    
    if len(new_string) > 5 and any(char in string.punctuation for char in new_string):
        return new_string

    return "No such string exists"