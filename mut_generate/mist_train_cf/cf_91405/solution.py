"""
QUESTION:
Create a function called `reverse_and_remove_duplicates` that takes a string as input and returns a new string that is the reversed version of the original string with no duplicate characters.
"""

def reverse_and_remove_duplicates(string):
    # Reverse the input string
    reversed_string = string[::-1]
    
    # Remove duplicate characters
    unique_string = ""
    for char in reversed_string:
        if char not in unique_string:
            unique_string += char
    
    return unique_string