"""
QUESTION:
Create a function `insert_at_position` that inserts a given value at a specified position in a singly linked list. The function should take the head of the linked list, the value to be inserted, and the position (0-indexed) as arguments, and return the updated head of the linked list. If the specified position is invalid (i.e., beyond the end of the list), the function should print an error message and return the original head.
"""

def insert_at_position(head, value, position):
    new_node = Node(value)

    if position == 0:
        new_node.next = head
        return new_node

    current = head
    previous = None
    current_position = 0

    while current_position < position:
        if current is None:
            print("Invalid position")
            return head
        previous = current
        current = current.next
        current_position += 1

    previous.next = new_node
    new_node.next = current

    return head

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None