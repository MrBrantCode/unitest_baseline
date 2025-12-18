"""
QUESTION:
Implement a function named `isStructurallyIdentical` that takes two parameters, `tree1` and `tree2`, representing the root nodes of two binary trees. The function should return `True` if the two binary trees are structurally identical (i.e., have the same structure and the same node values at each corresponding position), and `False` otherwise. The function should have a time complexity of O(n), where n is the number of nodes in the larger tree.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isStructurallyIdentical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is None or tree2 is None:
        return False
    
    if tree1.value != tree2.value:
        return False
    
    left_identical = isStructurallyIdentical(tree1.left, tree2.left)
    if not left_identical:
        return False
    
    right_identical = isStructurallyIdentical(tree1.right, tree2.right)
    if not right_identical:
        return False
    
    return True