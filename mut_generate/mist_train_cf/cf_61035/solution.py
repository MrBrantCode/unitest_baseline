"""
QUESTION:
Write a function named `reverseLinkedList` that takes the head of a linked list as input and reverses the linked list in-place, returning the new head. The function should achieve optimal space efficiency without using any data structures that scale with input size.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(head):
    current = head
    previous = None
    next_node = None

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous