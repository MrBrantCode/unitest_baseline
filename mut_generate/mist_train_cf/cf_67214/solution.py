"""
QUESTION:
Write a function named `delete` that takes a `key` as input, deletes the node with the given `key` from a singly linked list, and updates the list accordingly. The function should handle the cases where the node to be deleted is the head of the list and where the node to be deleted is not found in the list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def delete(self, key):
    cur = self.head

    if cur and cur.data == key:
        self.head = cur.next
        cur = None
        return

    prev = None
    while cur and cur.data != key:
        prev = cur
        cur = cur.next
    if cur is None:
        return

    prev.next = cur.next
    cur = None