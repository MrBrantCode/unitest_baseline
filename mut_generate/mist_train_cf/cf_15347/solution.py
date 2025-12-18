"""
QUESTION:
Create a function named `reverse_and_uppercase_string` that takes a string as input and returns a new string with all characters converted to uppercase and the order of characters reversed. The function should not use any built-in string reversal methods or functions.
"""

def reverse_and_uppercase_string(input_string):
    # Convert the string to uppercase
    uppercased_string = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            # Convert lowercase letters to uppercase
            uppercased_string += chr(ord(char) - 32)
        else:
            uppercased_string += char
    
    # Reverse the order of the characters
    reversed_string = ""
    for i in range(len(uppercased_string) - 1, -1, -1):
        reversed_string += uppercased_string[i]
    
    return reversed_string