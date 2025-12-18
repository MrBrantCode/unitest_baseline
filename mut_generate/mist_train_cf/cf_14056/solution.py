"""
QUESTION:
Write a function `isSameTree` that checks if two binary trees `p` and `q` are structurally identical and have the same node values. The function should take `p` and `q` as input and return `True` if the trees are the same, and `False` otherwise. Assume the trees have at most 1000 nodes each and node values are integers within the range of -1000 to 1000.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)