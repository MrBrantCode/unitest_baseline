"""
QUESTION:
Implement a function named `reverseLinkedList` that takes the head node of a linked list as input and returns the head node of the reversed linked list. The linked list nodes are defined with a value and a pointer to the next node. The input head node is guaranteed to be valid and not None.
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