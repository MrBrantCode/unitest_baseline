"""
QUESTION:
Implement a function `reverse_string` that takes a string as input and returns the reversed string using both a stack and a queue data structure. The function should have a time complexity of O(n), where n is the length of the input string, and include error handling for potential edge cases such as empty stack or queue.
"""

def reverse_string(s):
    stack = []
    queue = []

    for char in s:
        stack.append(char)
        queue.insert(0, char)

    reversed_string_stack = ""
    while stack:
        reversed_string_stack += stack.pop()

    return reversed_string_stack