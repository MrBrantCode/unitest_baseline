"""
QUESTION:
Implement a function named `reverse_string` that uses both a stack and a queue to reverse the order of characters in a given string. The function should have a time complexity of O(n), where n is the length of the input string, and include error handling for potential edge cases such as an empty stack or queue. Use two different data structures to implement the stack and queue.
"""

def reverse_string(string):
    stack = []
    queue = []

    for char in string:
        stack.append(char)
        queue.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string