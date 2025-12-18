"""
QUESTION:
Write a function named `reverse_stack` that takes a stack as input and returns the reversed stack without using any additional data structures. The original stack should not be modified or destroyed during the reversal process, and the function should have a time complexity of O(n), where n is the size of the stack.
"""

def reverse_stack(stack):
    if len(stack) == 1:  # Base case: stack with only one element
        return stack

    top = stack.pop()  # Remove the top element

    # Reverse the remaining stack
    reversed_stack = reverse_stack(stack)

    # Insert the top element at the bottom of the reversed stack
    insert_at_bottom(reversed_stack, top)

    return reversed_stack

def insert_at_bottom(stack, value):
    if len(stack) == 0:  # Base case: stack is empty
        stack.append(value)
        return

    top = stack.pop()  # Remove the top element

    # Insert the value at the bottom of the stack
    insert_at_bottom(stack, value)

    # Put the removed top element back on top of the stack
    stack.append(top)