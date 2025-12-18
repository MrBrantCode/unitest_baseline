"""
QUESTION:
Create a function called `reverse_string_dict` that takes a string as input and returns the reversed string using a dictionary. The function should map each character in the string to its reversed counterpart and then iterate through the string to construct the reversed string.
"""

def reverse_string_dict(s):
    char_dict = {}
    reversed_str = ""
    
    # Create a dictionary with all the characters from the string as keys and their reversed version as the values
    for i, char in enumerate(s):
        char_dict[char] = s[-i - 1]
        
    # Look up each character in the dictionary and add its value to a new string
    for char in s:
        reversed_str += char_dict[char]
        
    return reversed_str