"""
QUESTION:
Create a function called `reverse_string` that takes two parameters: `string` and `n`, where `string` is the input string and `n` is the number of characters to return from the end. The function should return the last `n` characters of the string in reverse order. If `n` is greater than or equal to the length of the string, return the entire string in reverse order. The function should be able to handle strings containing special characters, whitespace, and non-alphanumeric characters.
"""

def reverse_string(string, n):
    if n >= len(string):
        return string[::-1]  
    else:
        return string[-n:][::-1]