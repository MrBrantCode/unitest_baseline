"""
QUESTION:
Implement a function `reverse_string` that takes a string containing only alphabetic characters as input and returns the reversed string while preserving the original case of each letter. The function should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(input_string):
    stack = []
    
    # Push each character of the input string onto the stack
    for char in input_string:
        stack.append(char)
    
    # Pop each character from the stack and append it to the reversed string
    reversed_string = ""
    while stack:
        char = stack.pop()
        reversed_string += char
    
    return reversed_string