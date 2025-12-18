"""
QUESTION:
Implement a function called `reverse_string` that takes a string as input and returns the reversed string. Use a stack data structure to achieve this, without using any additional data structures that scale with the input size, thereby maintaining constant space complexity.
"""

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string