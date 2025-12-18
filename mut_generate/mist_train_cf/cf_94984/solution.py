"""
QUESTION:
Implement a function `to_lowercase(input_string)` that converts the input string to all lowercase without using any built-in string manipulation functions or methods. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def to_lowercase(input_string):
    lowercase_string = ""
    
    for char in input_string:
        if ord('A') <= ord(char) <= ord('Z'):  # Check if it is an uppercase letter
            lowercase_char = chr(ord(char) + 32)  # Convert to lowercase by adding 32 to ASCII value
            lowercase_string += lowercase_char
        else:
            lowercase_string += char
    
    return lowercase_string