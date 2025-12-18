"""
QUESTION:
Implement a function `insert_at_index` that inserts a new node with a given `element` at a specified `index` in a linked list. The function takes the `head` of the linked list, the `element`, and the `index` as parameters. The function should return the head of the modified linked list. The linked list is defined by a `Node` class with `element` and `next` attributes.
"""

class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

def insert_at_index(head, element, index):
    if index == 0:
        new_node = Node(element)
        new_node.next = head
        return new_node
    
    current_node = head
    current_index = 0
    
    while current_node and current_index < index - 1:
        current_node = current_node.next
        current_index += 1
    
    if not current_node:
        return head
    
    new_node = Node(element)
    new_node.next = current_node.next
    current_node.next = new_node
    
    return head