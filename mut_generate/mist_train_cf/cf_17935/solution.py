"""
QUESTION:
Write a function `insert_at_position(head, value, position)` that inserts a given value at a specified position in a singly linked list, where the position is specified as the index (starting from 0). The function should return the head of the updated linked list. The time complexity of the solution should be O(1) if the position is 0, and O(n) otherwise, where n is the number of nodes in the linked list.
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
    else:
        current = head
        for _ in range(position - 1):
            if current.next is None: 
                break
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        return head