"""
QUESTION:
Write a function `delete_node` that takes the head of a sorted linked list in ascending order and a value as input, and returns the head of the updated linked list after deleting the node with the given value. The linked list node structure is defined as a class `Node` with `data` and `next` attributes, where `data` is the node's value and `next` is a reference to the next node in the list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, value):
    # If the list is empty
    if head is None:
        return head

    # If the node to be deleted is the head
    if head.data == value:
        return head.next

    # Traverse through the linked list to find the node before the one to be deleted
    current = head
    while current.next is not None and current.next.data != value:
        current = current.next

    # If the node to be deleted is not found in the linked list
    if current.next is None:
        return head

    # Skip the node to be deleted
    current.next = current.next.next

    return head