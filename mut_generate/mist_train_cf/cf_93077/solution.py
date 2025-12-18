"""
QUESTION:
Write a function `isSameTree` that takes two binary trees `p` and `q` as input, where the trees have at most 1000 nodes each and the values of the nodes are integers within the range of -1000 to 1000. Return `True` if the trees are structurally identical and the nodes have the same value, and `False` otherwise.
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