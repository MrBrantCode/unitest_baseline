"""
QUESTION:
Design a function `are_identical(tree1, tree2)` that checks if two given binary trees `tree1` and `tree2` are identical. Each node in the binary trees contains an integer value and a character value. The function should return `True` if both the integer values and character values of the corresponding nodes are identical in both trees, and `False` otherwise. The function should handle cases where either one or both of the trees are empty (null).
"""

class Node:
    def __init__(self, value, char):
        self.value = value
        self.char = char
        self.left = None
        self.right = None

def are_identical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    
    if tree1 is None or tree2 is None:
        return False
    
    if tree1.value != tree2.value or tree1.char != tree2.char:
        return False
    
    return are_identical(tree1.left, tree2.left) and are_identical(tree1.right, tree2.right)