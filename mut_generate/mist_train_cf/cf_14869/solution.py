"""
QUESTION:
Write a function named `capitalize_string` that takes a string as an argument and returns the same string with the first letter capitalized and the first letter after each punctuation mark ('.', '!', '?', ':') capitalized. The function must have a time complexity of O(n), where n is the length of the string.
"""

def capitalize_string(string):
    new_string = ''
    capitalize = True
    
    for char in string:
        if capitalize and char.isalpha():
            char = char.upper()
            capitalize = False
        elif char in ['.', '!', '?', ':']:
            capitalize = True
        
        new_string += char
    
    return new_string