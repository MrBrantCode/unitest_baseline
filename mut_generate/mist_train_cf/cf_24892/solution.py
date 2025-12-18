"""
QUESTION:
Implement a function `has_cycle` that determines whether a given linked list contains a cycle. The function should take the head of the linked list as input and return a boolean value indicating the presence of a cycle. The linked list nodes are defined as `class ListNode: def __init__(self, x): self.val = x; self.next = None`.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    """
    Detects whether a cycle exists in a given linked list.

    Args:
    head (ListNode): The head of the linked list.

    Returns:
    bool: True if a cycle exists in the linked list, False otherwise.
    """
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True