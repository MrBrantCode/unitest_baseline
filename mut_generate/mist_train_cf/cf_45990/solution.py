"""
QUESTION:
Write a function named `remove_duplicates` that takes the head of a singly linked list as input and returns the head of the modified linked list with duplicates removed. Assume the linked list is unsorted and contains integer values.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return head

    visited = {head.data}
    current = head
    while current.next:
        if current.next.data in visited:
            current.next = current.next.next
        else:
            visited.add(current.next.data)
            current = current.next

    return head