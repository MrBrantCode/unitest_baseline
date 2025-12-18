"""
QUESTION:
Write a function `has_cycle(head)` that determines whether a cycle exists in a linked list given its head node. The function should return `True` if a cycle is detected and `False` otherwise. The function should run in linear time and use constant space.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    if head is None:
        return False
    slow_ptr, fast_ptr = head, head.next
    while fast_ptr is not None and fast_ptr.next is not None and slow_ptr != fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr == fast_ptr