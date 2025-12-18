"""
QUESTION:
Create a function called `clean_string` that takes a string as input. The function should remove all non-alphanumeric characters, remove duplicates, and return the modified string in ascending order. The function should be case-insensitive, treating uppercase and lowercase letters as the same character. If the input string is empty or contains no valid characters, the function should return an empty string.
"""

def clean_string(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Initialize a set to store the unique characters
    unique_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Check if the character is an alphabet or digit
        if char.isalnum():
            # Add the lowercase character to the set
            unique_chars.add(char)
    
    # Sort the unique characters in ascending order
    sorted_chars = sorted(unique_chars)
    
    # Convert the sorted characters to a string
    result = ''.join(sorted_chars)
    
    return result