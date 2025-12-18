"""
QUESTION:
Write a function `reverse_and_uppercase_string` that takes a string as input, converts it to uppercase without using any built-in string methods for uppercase conversion, reverses the order of its characters without using any built-in string reversal methods or functions, and returns the resulting string. The function should work with strings containing alphabetic characters and spaces.
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