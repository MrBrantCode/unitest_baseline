"""
QUESTION:
Create a function `insert_at_position(head, position, item)` to insert an item at a specified position in a circular linked list. The function should take the head of the circular linked list, the position where the item should be inserted, and the item to be inserted as input. The position can be any integer (positive, zero, or negative). The function should handle invalid positions by printing an error message and returning the original list without any modifications.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_position(head, position, item):
    # Check if position is valid
    if position < 0:
        print("Invalid position")
        return head

    # Create a new node
    new_node = Node(item)

    # If the list is empty, make the new node the head and point it to itself
    if head is None:
        new_node.next = new_node
        return new_node

    # If the position is 0, insert the new node before the head
    if position == 0:
        new_node.next = head
        temp = head
        while temp.next != head:
            temp = temp.next
        temp.next = new_node
        return new_node

    # Find the node at the given position
    current = head
    count = 0
    while count < position - 1:
        current = current.next
        count += 1
        # If we reach the end of the list before reaching the given position,
        # wrap around to the beginning of the list
        if current.next == head:
            current = head

    # Insert the new node after the current node
    new_node.next = current.next
    current.next = new_node
    return head