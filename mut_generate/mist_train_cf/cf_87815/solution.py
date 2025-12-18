"""
QUESTION:
Create a function called `concatenate_strings` that takes two strings as input. The function should remove any leading or trailing white spaces from both strings. If either string is empty after removing the white spaces, return the error message "Error: Input strings cannot be empty". If both strings are not empty, concatenate them and check if the concatenated string contains any alphanumeric characters. If it does, return the error message "Error: Input strings cannot contain alphanumeric characters". Otherwise, return the concatenated string.
"""

def concatenate_strings(string1, string2):
    # Remove leading and trailing white spaces
    string1 = string1.strip()
    string2 = string2.strip()
    
    # Check if either string is empty
    if not string1 or not string2:
        return "Error: Input strings cannot be empty"
    
    # Concatenate the strings
    concatenated_string = string1 + string2
    
    # Check if the concatenated string contains any alphanumeric characters
    if any(char.isalnum() for char in concatenated_string):
        return "Error: Input strings cannot contain alphanumeric characters"
    
    return concatenated_string