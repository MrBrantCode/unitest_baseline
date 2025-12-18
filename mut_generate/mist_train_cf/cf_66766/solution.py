"""
QUESTION:
Write a function named `delete` that takes in a `LinkedList` object and a node's `data` as input. The `LinkedList` object has a `head` node, and each node has a `data` value and a `next` node. The `delete` function should remove the node with the given `data` from the `LinkedList` and adjust the `next` pointers of the adjacent nodes accordingly. If the node to be deleted is the `head` node, the function should update the `head` of the `LinkedList`. If the `LinkedList` is empty or the node to be deleted is not found, the function should do nothing.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def delete(linked_list, data):
    if linked_list.head is None:
        return

    # If the data to be deleted is at the head of list
    if linked_list.head.data == data:
        linked_list.head = linked_list.head.next
        return

    current = linked_list.head
    while current.next:
        if current.next.data == data:
            current.next = current.next.next
            return
        current = current.next