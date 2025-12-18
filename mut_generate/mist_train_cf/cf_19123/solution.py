"""
QUESTION:
Write a function `convert_string` that takes a string as input and returns a string that contains only uppercase alphabetic characters and spaces, with no duplicate characters. The input string will only contain alphabetic characters, spaces, and punctuation marks. The function should not use built-in functions or methods to convert the string to uppercase or remove duplicate characters. The time complexity of the function should be O(n), where n is the length of the input string.
"""

def convert_string(string):
    uppercase_string = ""
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    for char in string:
        if char.isalpha() or char.isspace():
            uppercase_string += char.upper()
    
    unique_string = ""
    for char in uppercase_string:
        if char not in unique_string:
            unique_string += char
    
    return unique_string