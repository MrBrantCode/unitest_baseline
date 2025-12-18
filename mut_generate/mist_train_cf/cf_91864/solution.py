"""
QUESTION:
Create a function called `clean_string` that takes a string as input. The function should remove all non-alphanumeric characters, eliminate duplicate characters (in a case-insensitive manner), and return the resulting string in ascending order. If the input string is empty or contains no valid characters, the function should return an empty string.
"""

def clean_string(s):
    # Convert the string to lowercase
    s = s.lower()
    
    # Initialize a set to store the unique characters
    unique_chars = set()
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an alphabet or digit
        if char.isalnum():
            # Add the lowercase character to the set
            unique_chars.add(char.lower())
    
    # Sort the unique characters in ascending order
    sorted_chars = sorted(unique_chars)
    
    # Convert the sorted characters to a string
    result = ''.join(sorted_chars)
    
    return result