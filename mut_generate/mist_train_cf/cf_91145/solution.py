"""
QUESTION:
Implement the function `insertNodeAtPosition` that takes the head pointer of a singly linked list, a node value, and a 1-based position as input and returns the head pointer of the modified linked list after inserting the node at the specified position.

The linked list will have at least one node and at most 10^3 nodes, each with a distinct positive integer value at most 10^3. The position given will always be valid, i.e., a positive integer less than or equal to the number of nodes in the linked list plus one.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insertNodeAtPosition(head, value, position):
    new_node = Node(value)
    if position == 1:
        new_node.next = head
        return new_node

    current = head
    for _ in range(position - 2):
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head