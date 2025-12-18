"""
QUESTION:
Create a function called `preserve_uppercase` that takes a string of alphanumeric characters as input and returns a new string containing only the uppercase alphabetical elements from the original string. The function should not include any characters that are not uppercase letters.
"""

def entrance(sequence):
    # Create an empty string to store the result
    result = ''
    
    # Iterate through each character in the sequence
    for character in sequence:
        
        # Check if the current character is an uppercase letter
        if character.isupper():
          
            # If it is, append it to the result string
            result += character
    
    # Return the result string
    return result