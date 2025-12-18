"""
QUESTION:
Create a function `reverse_concatenate` that takes a string as input and returns a new string where the original string is concatenated with a reversed copy of itself. The reversed copy should only include alphabetic characters from the original string, ignoring any non-alphabetic characters, and should be case-insensitive, treating uppercase and lowercase characters as the same.
"""

def reverse_concatenate(string):
    reversed_copy = ""
    
    # Iterate through each character in the string in reverse order
    for char in string[::-1]:
        # Check if the character is alphabetic
        if char.isalpha():
            # Convert the character to lowercase
            char = char.lower()
            # Add the character to the reversed copy
            reversed_copy += char
    
    # Concatenate the original string with the reversed copy
    result = string + reversed_copy
    
    return result