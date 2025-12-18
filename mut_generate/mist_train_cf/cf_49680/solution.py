"""
QUESTION:
Implement a function `reverse_string` that takes a string as input and returns the reversed string without using built-in reverse functions (e.g. `reversed()`, `[::-1]`). The function should use a stack data structure to achieve this. The stack should support `push`, `pop`, and `is_empty` operations.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "Empty Stack"

    def is_empty(self):
        return len(self.stack) == 0


def reverse_string(input_string):
    stack = Stack()
    for character in input_string:
        stack.push(character)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string