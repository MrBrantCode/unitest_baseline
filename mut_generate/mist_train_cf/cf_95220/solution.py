"""
QUESTION:
Implement the `add_node_at_index` function to insert a new node with a given value at a specified index in a linked list. The function takes three parameters: the head of the linked list, the index at which to insert the new node, and the value of the new node. If the index is out of range (less than 0 or greater than the length of the linked list), the function should return the original linked list unchanged.
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