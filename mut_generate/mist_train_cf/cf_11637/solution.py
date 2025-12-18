"""
QUESTION:
Write a function named `reverse_stack` that reverses the elements of a given stack without using any additional data structures. The stack is implemented using a list. The function should modify the original stack and return it.
"""

def reverse_stack(stack):
    """
    Reverses the elements of a given stack without using any additional data structures.
    
    Args:
    stack (list): The input stack implemented as a list.
    
    Returns:
    list: The modified stack with elements reversed.
    """
    if len(stack) == 0:
        return stack
    
    # Remove the top element from the stack
    top = stack.pop()
    
    # Reverse the remaining stack
    reverse_stack(stack)
    
    # Insert the top element at the bottom of the stack
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    """
    Inserts an item at the bottom of the stack without using any additional data structures.
    
    Args:
    stack (list): The input stack implemented as a list.
    item: The item to be inserted at the bottom of the stack.
    """
    if len(stack) == 0:
        stack.append(item)
    else:
        # Remove all the elements from the stack and insert them at the bottom
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)