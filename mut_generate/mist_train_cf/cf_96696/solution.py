"""
QUESTION:
Write a function `reverseLinkedList(head)` to reverse a linked list in place with a time complexity of O(n) and using only constant extra space (O(1)). The function should not use any additional data structures or modify the values in the nodes of the linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    if head is None or head.next is None:
        return head

    # Initialize three pointers: prev, curr, and next
    prev = None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # The new head of the reversed list will be the last node
    head = prev
    return head