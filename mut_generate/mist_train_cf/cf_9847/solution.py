"""
QUESTION:
Write a function called `reverseLinkedList` that takes the head node of a linked list as input and returns the head node of the reversed linked list. The linked list node is defined as a class with `val` and `next` attributes. Assume the input head node is always valid and not `None`.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous