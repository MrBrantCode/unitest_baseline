"""
QUESTION:
Write a function called `insert_at_position` that inserts a given value at a specified position in a sorted singly linked list, ensuring the list remains sorted in ascending order after the insertion. The position is specified as the index (starting from 0) where the value should be inserted. The function should have a time complexity of O(n), where n is the length of the linked list. The function should take three parameters: the head of the linked list, the value to be inserted, and the position where the value should be inserted.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def insert_at_position(head, value, position):
    # Create a new node with the given value
    new_node = Node(value)

    # If the position is 0, update the new node's next pointer to the head and return it as the new head
    if position == 0:
        new_node.next = head
        return new_node

    # Iterate through the linked list until we reach the position where the value should be inserted
    current = head
    for _ in range(position - 1):
        if current.next is None:
            break
        current = current.next

    # Update the pointers to insert the new node into the linked list
    new_node.next = current.next
    current.next = new_node

    return head