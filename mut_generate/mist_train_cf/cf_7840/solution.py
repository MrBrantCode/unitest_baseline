"""
QUESTION:
Implement a function named `isStructurallyIdentical` that checks if two binary trees are structurally identical or not. The function takes two parameters, `tree1` and `tree2`, representing the root nodes of two binary trees. The function should return `True` if the trees are structurally identical and `False` otherwise.

The function should satisfy the following constraints:

- The node values of the binary trees are integers.
- The binary trees can have a maximum of 10^5 nodes.
- The binary trees can have a maximum depth of 1000.
- The time complexity of the solution should be optimized to O(n), where n is the number of nodes in the larger tree.
- The space complexity of the solution should be optimized to O(h), where h is the height of the larger tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isStructurallyIdentical(tree1, tree2):
    # Check if both trees are None
    if tree1 is None and tree2 is None:
        return True
    
    # Check if one tree is None while the other is not
    if tree1 is None or tree2 is None:
        return False
    
    # Recursively check the left subtrees
    left_identical = isStructurallyIdentical(tree1.left, tree2.left)
    if not left_identical:
        return False
    
    # Recursively check the right subtrees
    right_identical = isStructurallyIdentical(tree1.right, tree2.right)
    if not right_identical:
        return False
    
    # If all recursive calls return True, the trees are structurally identical
    return True