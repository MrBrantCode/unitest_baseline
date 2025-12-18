"""
QUESTION:
Implement a function `reverseLinkedList(head)` that reverses a singly linked list in place using constant extra space (O(1)) and achieving a time complexity of O(n), where n is the length of the linked list. The function should not modify the values in the nodes of the linked list and should not use any additional data structures. The function should return the head of the reversed linked list.
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