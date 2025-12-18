"""
QUESTION:
Implement a recursive function `empty_stack(stack)` that takes a list (representing a stack) as input and empties it by continuously removing elements from the top until the stack is empty. The function should not return anything, but instead modify the original stack in-place.
"""

def empty_stack(stack):
    if len(stack) != 0:
        stack.pop()
        return empty_stack(stack)