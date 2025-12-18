"""
QUESTION:
Implement the function `insertNodeAtPosition` that takes in the head pointer of a singly linked list, the value of the node to be inserted, and the position at which the node should be inserted. The position is 1-based. The function should return the head pointer of the modified linked list.

The linked list will have at least one node and at most 10^3 nodes, and each node has a distinct positive integer value, which will be at most 10^3. The position given will always be valid, i.e., it will be a positive integer less than or equal to the number of nodes in the linked list plus one.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insertNodeAtPosition(head, value, position):
    # Create a new node with the given value
    new_node = Node(value)

    # If the position is 1, insert the new node at the beginning
    if position == 1:
        new_node.next = head
        return new_node

    # Traverse the linked list to find the node at the position
    current = head
    for _ in range(position - 2):
        current = current.next

    # Insert the new node after the current node
    new_node.next = current.next
    current.next = new_node

    return head