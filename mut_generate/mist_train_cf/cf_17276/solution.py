"""
QUESTION:
Create a function named `create_new_string` that takes one string argument, filters out only the uppercase letters from the input string, and returns the filtered string if it has a length greater than 5 and contains at least one special character. If the conditions are not met, return "No such string exists".
"""

import string

def create_new_string(original_string):
    new_string = "".join(filter(str.isupper, original_string))
    return new_string if len(new_string) > 5 and any(char in string.punctuation for char in new_string) else "No such string exists"