"""
QUESTION:
Reverse a singly linked list given only its head pointer, without using any extra space or creating a new list, and achieve a time complexity of O(n), where n is the number of nodes in the linked list. Implement the reversal function `reverseLinkedList(head)`.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev