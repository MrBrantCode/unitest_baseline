"""
QUESTION:
Given a sorted singly linked list and a value to be inserted, write a function `insert_at_position(head, value, position)` that inserts the value at the specified position in the linked list while maintaining the sorted order. The position is 0-indexed and the time complexity should be O(n), where n is the length of the linked list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def insert_at_position(head, value, position):
    new_node = Node(value)

    if position == 0:
        new_node.next = head
        return new_node

    current = head
    for _ in range(position - 1):
        if current.next is None:
            break
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head