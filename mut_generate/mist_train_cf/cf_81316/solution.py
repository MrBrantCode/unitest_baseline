"""
QUESTION:
Implement a function named `reverse` that reverses a singly linked list of integers in-place, without creating a new linked list. The function should modify the input linked list so that the order of its elements is reversed.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev