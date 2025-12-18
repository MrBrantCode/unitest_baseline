"""
QUESTION:
Write a function called `convert_to_uppercase` that takes a string as input and returns the string with all lowercase letters converted to uppercase. The function should not use any built-in string methods or external libraries, and should handle all types of characters, including alphabets, numbers, and special characters. The function should work efficiently for strings of any length.
"""

def convert_to_uppercase(string):
    uppercase_string = ""
    # Iterate over each character in the string
    for char in string:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert lowercase letter to uppercase by subtracting 32 from its ASCII value
            uppercase_char = chr(ord(char) - 32)
        # Return the character as is if it's already uppercase or not a letter
        else:
            uppercase_char = char
        # Append the uppercase character to the new string
        uppercase_string += uppercase_char
    return uppercase_string