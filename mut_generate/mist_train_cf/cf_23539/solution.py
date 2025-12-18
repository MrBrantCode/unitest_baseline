"""
QUESTION:
Create a function named `deleteNode` that removes a specified node from a singly linked list. The function should take two parameters: the head of the linked list and the value of the node to be deleted. The function should return the updated head of the linked list after deletion. Assume that the node to be deleted exists in the linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(head, node):
    prev = None
    current = head
    # traverse the list until node is found
    while current is not None:
        if current.data == node:
            break
        prev = current
        current = current.next
    # if the node is the first node
    if prev is None:
        head = current.next
    else:
        prev.next = current.next
    return head