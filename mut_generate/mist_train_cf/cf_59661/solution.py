"""
QUESTION:
Write a function `get_kth_from_last` that takes the head of a linked list and an integer `k` as input, and returns the value of the `k`th node from the last node in the linked list. The function should traverse the linked list only once and return `None` if `k` is out of bounds.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def get_kth_from_last(head, k):
    p1 = head
    p2 = head

    # Move p2 forward k elements in the linked list.
    for i in range(k):
        if p2 is None:
            return None  # out of bounds
        p2 = p2.next

    # Move both pointers until p2 hits the end.
    while p2:
        p1 = p1.next
        p2 = p2.next

    # Since p2 started k elements ahead, p1 is now the kth from last element.
    return p1.data