"""
QUESTION:
Create a function named `concatenate_strings` that takes two strings as input. The function should remove any leading or trailing white spaces from both strings and concatenate them. However, if either string is empty after removing white spaces, it should return an error message "Error: Input strings cannot be empty". Additionally, if the concatenated string contains any alphanumeric characters, it should return an error message "Error: Input strings cannot contain alphanumeric characters".
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