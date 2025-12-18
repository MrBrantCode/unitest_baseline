"""
QUESTION:
Write a function called `isIdentical` that takes two binary trees `tree1` and `tree2` as input and returns a boolean indicating whether they are identical. Two trees are considered identical if they have the same structure and the same node values. Assume that `None` is used to denote the absence of a subtree or the end of a tree.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isIdentical(tree1, tree2):
    # Case 1: Both trees are null, which means they are identical
    if tree1 is None and tree2 is None:
        return True

    # Case 2: One of the trees is null, but the other is not
    # indicates they are not identical
    if tree1 is None or tree2 is None:
        return False

    # Case 3: If the value of the two nodes is the same,
    # we need to check if the left subtree and right subtree are identical
    if tree1.val == tree2.val:
        return isIdentical(tree1.left, tree2.left) and isIdentical(tree1.right, tree2.right)
    
    return False