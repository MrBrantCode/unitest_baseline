"""
QUESTION:
Write a function named `reverse_linked_list` that takes the head of a linked list as input and returns the head of the reversed linked list. The function must only use a stack data structure to store nodes temporarily and should not use any extra space that scales with input size except for the recursion stack.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    This function takes the head of a linked list as input, reverses the linked list using a stack data structure, 
    and returns the head of the reversed linked list.
    
    Args:
    head (ListNode): The head of the linked list to be reversed.
    
    Returns:
    ListNode: The head of the reversed linked list.
    """
    
    # Initialize a stack to store nodes temporarily
    stack = []
    
    # Traverse the linked list and push each node onto the stack
    current = head
    while current:
        # Push the current node onto the stack
        stack.append(current)
        # Move to the next node in the linked list
        current = current.next
    
    # Initialize the head of the reversed linked list
    new_head = None
    
    # Pop each node off the stack and insert it as the head of the new linked list
    while stack:
        # Pop the top node off the stack
        node = stack.pop()
        # Insert the popped node as the head of the new linked list
        node.next = new_head
        # Update the head of the new linked list
        new_head = node
    
    # Return the head of the reversed linked list
    return new_head