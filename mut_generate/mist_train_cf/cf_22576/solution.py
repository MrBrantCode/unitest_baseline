"""
QUESTION:
Write a function named "remove_special_chars" that takes a string as input and returns the modified string without any spaces, punctuation, or special characters, only containing alphanumeric characters. The order of the characters in the output string should be the same as the input string. The input string will not be empty and may contain uppercase and lowercase letters, numbers, spaces, punctuation marks, and special characters. The solution should have a time complexity of O(n), where n is the length of the input string, and cannot use built-in functions or libraries that directly solve this problem.
"""

def remove_special_chars(s):
    # Initialize an empty string to store the modified string
    modified_string = ""
    
    # Iterate over each character in the input string
    for char in s:
        # Check if the character is alphanumeric
        if char.isalnum():
            # Append the alphanumeric character to the modified string
            modified_string += char
    
    # Return the modified string
    return modified_string