"""
QUESTION:
Write a function `reverseLinkedList(head)` that takes the head of a singly linked list as input and returns the head of the reversed linked list. The function should not use any extra space or create a new list, and its time complexity should be O(n), where n is the number of nodes in the linked list.
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