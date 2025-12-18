"""
QUESTION:
Write a function called `add_node_at_index` that takes in a linked list, an integer index, and a value as input, and returns the modified linked list with a new node containing the given value inserted at the specified index. If the index is less than 0 or greater than or equal to the length of the linked list, the function should return the original linked list unchanged.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def add_node_at_index(linked_list, index, value):
    if index < 0:
        return linked_list

    new_node = Node(value)

    if index == 0:
        new_node.next = linked_list
        return new_node

    current = linked_list
    prev = None
    current_index = 0

    while current and current_index < index:
        prev = current
        current = current.next
        current_index += 1

    if current_index == index:
        prev.next = new_node
        new_node.next = current

    return linked_list