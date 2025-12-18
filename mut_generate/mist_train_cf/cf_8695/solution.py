"""
QUESTION:
Write a function `reverse_string` that takes a string as input, removes leading and trailing whitespace, converts to lowercase, and returns the reversed string without using any built-in string manipulation functions or libraries. The function should handle strings with special characters and numbers and have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(string):
    # Remove leading and trailing whitespace
    string = string.strip()
    
    # Convert string to lowercase
    result = ""
    for char in string:
        if ord('A') <= ord(char) <= ord('Z'):
            result += chr(ord(char) + 32)
        else:
            result += char
    
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    
    # Iterate through each character in the string, starting from the end
    for i in range(len(result)-1, -1, -1):
        # Append the character to the reversed string
        reversed_string += result[i]
    
    return reversed_string