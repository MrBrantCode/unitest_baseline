"""
QUESTION:
Implement a function `reverse_string(string)` that takes a string as input and returns the reversed string using a stack data structure. The function should achieve a time complexity of O(n), where n is the length of the string, and maintain constant space complexity by only using the input string and the stack, without any additional data structures.
"""

def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string