"""
QUESTION:
Insert a value at a specific index in a doubly linked list. Create a function `insert_at_index` that takes the head of a doubly linked list, an integer index, and a value as input. The function should return the head of the modified list. The index is 0-indexed, and if the index is out of range, the function should return the original list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_index(head, index, value):
    """
    Inserts a value at a specific index in a doubly linked list.

    Args:
        head (Node): The head of the doubly linked list.
        index (int): The index at which to insert the value (0-indexed).
        value (any): The value to insert.

    Returns:
        Node: The head of the modified list.
    """
    new_node = Node(value)
    
    # Check if the index is out of range
    if index < 0:
        return head
    
    # Handle insertion at the head of the list
    if index == 0:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        return new_node

    # Traverse the list to find the insertion point
    current = head
    current_index = 0
    while current is not None and current_index < index - 1:
        current = current.next
        current_index += 1

    # Check if the index is out of range
    if current is None:
        return head

    # Insert the new node
    new_node.next = current.next
    new_node.prev = current
    if current.next is not None:
        current.next.prev = new_node
    current.next = new_node

    return head