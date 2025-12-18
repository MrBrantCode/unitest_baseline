"""
QUESTION:
Write a function `reverse_linked_list` that takes the head of a singly linked list as input and returns the head of the reversed linked list. The function should run in O(n) time, where n is the number of nodes in the linked list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_linked_list(head):
    """
    Reverses a singly linked list in O(n) time.

    Args:
    head (ListNode): The head of the singly linked list.

    Returns:
    ListNode: The head of the reversed linked list.
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # Store the next node
        curr.next = prev      # Reverse the current node's pointer
        prev = curr           # Advance the prev pointer one position
        curr = next_node      # Advance the curr pointer one position
    return prev               # Return the reversed linked list