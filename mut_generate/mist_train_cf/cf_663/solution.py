"""
QUESTION:
Convert a given string with no spaces to a string with underscores (_) in all spaces between words, removing punctuation marks, handling multiple consecutive spaces, and ignoring non-alphabet characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. 

The function, named `convert_string`, takes a string as input and returns the converted string.
"""

def convert_string(string):
    # Remove leading and trailing spaces
    string = string.strip()
    
    # Create a variable to store the converted string
    converted_string = ''
    
    # Create a variable to keep track of the previous character
    prev_char = ''
    
    # Iterate over each character in the string
    for char in string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Check if the previous character is a space
            if prev_char == ' ':
                # If the previous character is a space, add an underscore to the converted string
                converted_string += '_'
                
            # Add the current character to the converted string
            converted_string += char
            
        # Update the previous character
        prev_char = char
    
    return converted_string