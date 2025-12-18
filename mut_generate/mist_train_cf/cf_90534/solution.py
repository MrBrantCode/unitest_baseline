"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns its reverse. The function should be case-insensitive, ignore any leading or trailing whitespace characters, and handle strings containing special characters and numbers. The function should not use any built-in string manipulation functions or libraries and have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(string):
    # Remove leading and trailing whitespace
    string = string.strip()
    
    # Convert string to lowercase
    string = string.lower()
    
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    
    # Iterate through each character in the string, starting from the end
    for i in range(len(string)-1, -1, -1):
        # Append the character to the reversed string
        reversed_string += string[i]
    
    return reversed_string