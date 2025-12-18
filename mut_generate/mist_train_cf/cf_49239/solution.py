"""
QUESTION:
Create a function called `create_pyramid` that constructs a pyramid data structure using a list of integers, where each parent node can have a maximum of three child nodes. The function should take a list of integers as input, and the pyramid should be constructed in a depth-first manner. The input list will contain 36 integers ranging from 1 to 50 in random order.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def create_pyramid(values):
    if not values: 
        return None
    root = Node(values.pop(0))
    def add_children(parent, values):
        if values and len(parent.children) < 3:
            child = Node(values.pop(0))
            parent.children.append(child)
            for _ in range(3):
                add_children(child, values)
    add_children(root, values)
    return root