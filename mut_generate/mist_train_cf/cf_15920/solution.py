"""
QUESTION:
Write a function `reverse_concatenate(string)` that takes a string as input and returns a new string created by concatenating the original string with its reversed alphabetic characters (ignoring non-alphabetic characters and treating uppercase and lowercase letters as the same).
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