"""
QUESTION:
Create a function `replace_odd_chars` that takes a string of up to 100 characters as input. The string may contain uppercase letters, lowercase letters, spaces, and special characters. Replace the characters at odd index positions with '#' and return the modified string. If the input string exceeds 100 characters, return an error message "Error: String exceeds maximum length of 100 characters".
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