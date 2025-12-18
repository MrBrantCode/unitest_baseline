"""
QUESTION:
Create a function called `reverse_string` that takes a string of alphabetic characters as input and returns the reversed string. The function should use a stack data structure and have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string