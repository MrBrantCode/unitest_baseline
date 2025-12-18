"""
QUESTION:
Create a function named `longest_string` that takes two strings as arguments. The function should return the longest string after removing any duplicate characters. The length of the returned string should be equal to the length of the longer input string.
"""

def longest_string(string1, string2):
    combined_string = string1 + string2
    unique_characters = ""
    
    for char in combined_string:
        if char not in unique_characters:
            unique_characters += char
    
    if len(string1) >= len(string2):
        return unique_characters[:len(string1)]
    else:
        return unique_characters[:len(string2)]