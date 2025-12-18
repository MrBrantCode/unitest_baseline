"""
QUESTION:
Write a function `delete_node(node)` to delete a given node from a singly linked list when only the node to be deleted is accessible, not the head of the list. The function should handle the case where the given node is the last node in the list and cannot be deleted.
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