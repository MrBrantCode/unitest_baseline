"""
QUESTION:
Write a function `delete_node(node)` that deletes a given node from a singly linked list. The function can only access the node to be deleted and not the head of the linked list. If the given node is the last node, it cannot be deleted.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(node):
    if node is None or node.next is None:
        # Cannot delete the last node
        return
    
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    
    # Free memory for next node
    next_node = None