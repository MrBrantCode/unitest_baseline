"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string. Implement the function using a stack data structure and ensure it maintains a constant space complexity.
"""

def reverse_string(string):
    stack = []  

    for char in string:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string