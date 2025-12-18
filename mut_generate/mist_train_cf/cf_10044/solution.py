"""
QUESTION:
Write a function `convertToDoublyLinkedList` that converts a singly linked list into a doubly linked list. The function should take the head of the singly linked list as input and return the head of the converted doubly linked list. The function should assume that the input linked list nodes have `value`, `next`, and `prev` attributes, where `next` points to the next node in the list and `prev` points to the previous node in the list. If the input list is empty, the function should return `None`.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def convertToDoublyLinkedList(head):
    if head is None:
        return None

    current = head
    prev = None

    while current:
        current.prev = prev
        prev = current
        current = current.next

    return head