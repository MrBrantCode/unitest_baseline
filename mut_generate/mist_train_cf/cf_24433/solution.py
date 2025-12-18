"""
QUESTION:
Write a function named `get_nth_node` that retrieves the nth node of a linked list. The function should take two parameters: the head of the linked list and an integer n representing the position of the node to be retrieved. Assume 1-indexing (the head is the first node) and the linked list has at least n nodes.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_nth_node(head, n):
    """
    Retrieves the nth node of a linked list.

    Args:
    head (ListNode): The head of the linked list.
    n (int): The position of the node to be retrieved (1-indexed).

    Returns:
    ListNode: The nth node of the linked list.
    """
    current = head
    for _ in range(n - 1):
        current = current.next
    return current