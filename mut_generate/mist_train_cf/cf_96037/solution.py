"""
QUESTION:
Create a function `delete_last_occurrence(head, item)` to delete the last occurrence of a specific item from a singly linked list given the head of the list and the item to be deleted. The function should return the head of the modified list. If the list is empty or the item is not found, return the head as is. The function should only modify the original list and should not create a new list.
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