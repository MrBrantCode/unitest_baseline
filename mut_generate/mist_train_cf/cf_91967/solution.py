"""
QUESTION:
Implement a function named `reverse_string` that takes an input string of only alphabetic characters and returns the reversed string using a stack with a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)
    
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string