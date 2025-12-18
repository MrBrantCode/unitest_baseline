"""
QUESTION:
Design a function `reverseLinkedList(head)` that takes the head of a singly linked list as input and reverses the linked list in O(n) time and O(1) space. The function should return the updated head of the reversed linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    if head is None or head.next is None:
        return head

    prev = None
    current = head
    next_node = None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    head = prev
    return head