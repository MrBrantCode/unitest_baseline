"""
QUESTION:
Implement a function named `reverse_string` that takes a string as input and returns the reversed string using a stack data structure. The function should follow the Last-In-First-Out (LIFO) principle to reverse the string efficiently. The input string can contain any characters, and the function should return the reversed string without any modifications to the original input.
"""

def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string