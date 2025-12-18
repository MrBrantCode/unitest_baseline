"""
QUESTION:
Implement a function `reverse(node)` that reverses a doubly linked list in-place. The function takes a node from the linked list as input and returns the new head of the reversed list. The function should handle edge cases such as an empty or single-node linked list and preserve the original structure of the linked list without using any extra data structures.
"""

class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None
        self.prev = None

def reverse(node): 
    if node is None: 
        return None 
    elif node.next is None:
        return node 

    current = node 
    while current is not None: 
        temp = current.prev 
        current.prev = current.next 
        current.next = temp 
        node = current 
        current = current.prev 

    return node