"""
QUESTION:
Create a function `delete_last_occurrence(head, item)` that takes the head of a singly linked list and an item as input, and returns the head of the modified list after deleting the last occurrence of the item. The function should handle cases where the list is empty, the head node is to be deleted, or the item is not found in the list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_last_occurrence(head, item):
    # If list is empty, return None
    if head is None:
        return None

    # If head node is to be deleted
    if head.data == item and head.next is None:
        return None

    # Traverse the list until the second last node
    prev = None
    curr = head
    while curr.next:
        if curr.next.data == item:
            prev = curr
        curr = curr.next

    # If item is not found in the list
    if prev is None:
        return head

    # Remove the last occurrence of item
    prev.next = prev.next.next

    return head