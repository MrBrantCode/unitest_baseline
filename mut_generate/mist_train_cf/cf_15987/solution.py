"""
QUESTION:
Create a function called `ReverseDoublyLinkedList` that takes the head of a doubly linked list as input and reverses the list in place without using any extra space or auxiliary data structures, returning the new head of the reversed list. The doubly linked list node is assumed to have `next` and `prev` pointers.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def ReverseDoublyLinkedList(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next

        current.next = prev
        current.prev = next_node

        prev = current
        current = next_node

    head = prev

    return head