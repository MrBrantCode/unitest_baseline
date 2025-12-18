"""
QUESTION:
Write a function called `reverseKGroup` that takes the head of a linked list and an integer `k` as input. The function should reverse the nodes of the linked list `k` at a time and return the modified list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    """
    Reverses the nodes of a linked list k at a time.

    Args:
        head (ListNode): The head of the linked list.
        k (int): The number of nodes to reverse at a time.

    Returns:
        ListNode: The head of the modified linked list.
    """
    curr = head
    prev = None
    
    count = 0
    
    while curr is not None and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1
    
    if curr is not None:
        head.next = reverseKGroup(curr, k)
    
    return prev