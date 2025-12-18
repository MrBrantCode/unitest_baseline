"""
QUESTION:
Write a function named `reverse` that takes the head of a singly linked list as input and returns the head of the reversed linked list. The function should reverse the linked list in place, meaning it should not create a new linked list, but instead modify the existing one.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    current = head
    prev = None
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head