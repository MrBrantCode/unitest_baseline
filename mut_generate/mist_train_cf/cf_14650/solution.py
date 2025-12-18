"""
QUESTION:
Write a function `replace_odd_chars` that takes a string as input and returns a modified string with all characters at odd index positions replaced with '#'. The input string can contain uppercase letters, lowercase letters, spaces, and special characters. The length of the input string should not exceed 100 characters. If the length exceeds 100 characters, return an error message.
"""

def replace_odd_chars(string):
    if len(string) > 100:
        return "Error: String exceeds maximum length of 100 characters"
    
    modified_string = ''
    for i in range(len(string)):
        if i % 2 != 0:
            modified_string += '#'
        else:
            modified_string += string[i]
    
    return modified_string