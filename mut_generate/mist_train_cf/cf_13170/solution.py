"""
QUESTION:
Create a function called `is_identical` that takes two binary search trees as input, where each node in the trees has an integer value and a color attribute that can be either "red" or "black". The function should return a boolean value indicating whether the two trees have the same structure and the same values in their nodes, considering the "color" attribute as well.
"""

class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None

def is_identical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    
    if tree1.value != tree2.value or tree1.color != tree2.color:
        return False
    
    return is_identical(tree1.left, tree2.left) and is_identical(tree1.right, tree2.right)