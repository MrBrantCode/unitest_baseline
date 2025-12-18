"""
QUESTION:
Create a function called `transform_string` that takes a string as input and returns a new string where all lowercase characters have been swapped with their uppercase equivalents and vice versa. The function should handle both alphabetic and non-alphabetic characters.
"""

def transform_string(string):
    transformed_string = ""
    
    for char in string:
        if char == char.lower():
            transformed_string += char.upper()
        else:
            transformed_string += char.lower()
    
    return transformed_string