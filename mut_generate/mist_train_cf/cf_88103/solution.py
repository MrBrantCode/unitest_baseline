"""
QUESTION:
Write a function `add_node` that takes in a linked list and two parameters: `value` (the data for the new node) and `index` (the position where the new node should be inserted). The function should insert the new node at the specified `index` and return the modified linked list. If the `index` is less than -1 or greater than or equal to the length of the linked list, the function should raise an `IndexOutOfRangeException`. If the `index` is -1, the new node should be appended to the end of the linked list.
"""

def add_node(head, value, index):
    """
    Inserts a new node with the given value at the specified index in the linked list.

    Args:
    head (Node): The head of the linked list.
    value (any): The value for the new node.
    index (int): The position where the new node should be inserted.

    Returns:
    Node: The head of the modified linked list.

    Raises:
    IndexOutOfRangeException: If the index is less than -1 or greater than or equal to the length of the linked list.
    """

    # Check if the index is valid
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next

    if index < -1 or index > length:
        raise IndexOutOfRangeException("Index out of range")

    # Create a new node
    new_node = Node(value)

    # If the index is -1, append the new node to the end of the linked list
    if index == -1:
        if head is None:
            return new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
            return head

    # If the index is 0, insert the new node at the beginning of the linked list
    if index == 0:
        new_node.next = head
        return new_node

    # Insert the new node at the specified index
    current = head
    for _ in range(index - 1):
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class IndexOutOfRangeException(Exception):
    pass