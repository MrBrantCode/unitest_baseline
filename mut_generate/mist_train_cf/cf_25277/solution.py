"""
QUESTION:
Write a function `reverse_linked_list` that takes the head of a singly linked list as input and reverses the linked list in-place without using any additional data structures.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_linked_list(head):
    """
    Reverses a singly linked list in-place.

    Args:
    head: The head of the singly linked list.

    Returns:
    The head of the reversed linked list.
    """
    prev = None
    while head:
        # Store the successor of the current node
        next_node = head.next
        
        # Link the current node to its predecessor
        head.next = prev
        
        # Move to the next node
        prev = head
        head = next_node
    
    # Return the head of the reversed linked list
    return prev