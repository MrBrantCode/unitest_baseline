"""
QUESTION:
Create a function named `replace_characters` that takes a string as input and returns a new string where all instances of 'A' are replaced with 'Z', 'B' with 'Y', 'C' with 'X', and 'D' with 'W', while preserving the original case sensitivity. The function should handle cases where multiple instances of 'A', 'B', 'C', or 'D' are adjacent to each other and cases where the input string contains characters other than 'A', 'B', 'C', or 'D'. The function should have a time complexity of O(n), where n is the length of the string.
"""

def replace_characters(string):
    mapping = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W'}
    result = ''
    
    for char in string:
        if char.upper() in mapping:
            if char.isupper():
                result += mapping[char.upper()]
            else:
                result += mapping[char.upper()].lower()
        else:
            result += char
    
    return result