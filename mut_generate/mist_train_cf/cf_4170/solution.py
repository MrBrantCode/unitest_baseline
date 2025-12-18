"""
QUESTION:
Implement a function called `reverse_string` that takes a string as input and returns the reversed string. The function should use a stack data structure to reverse the string in-place and have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string