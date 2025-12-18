"""
QUESTION:
Write a function `getMaxLevelSum` that finds the height of a binary tree and returns the maximum sum of values of nodes at any level in the tree. The function should take the root of the binary tree as input, where each node is represented as an object with `val`, `left`, and `right` attributes. The function should return an integer representing the maximum sum of values at any level in the tree.

Additionally, write a function `isValidBST` that checks if a binary tree is a valid binary search tree. The function should take the root of the binary tree as input and return a boolean indicating whether the tree is a valid binary search tree. The binary tree should be implemented using a doubly linked list, where each node has a reference to both its left and right child nodes as well as its parent node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMaxLevelSum(root):
    def getHeight(node):
        if node is None:
            return 0
        return max(getHeight(node.left), getHeight(node.right)) + 1

    def getMaxSum(node, level):
        if node is None:
            return 0
        if level == 0:
            return node.val
        return getMaxSum(node.left, level - 1) + getMaxSum(node.right, level - 1)

    height = getHeight(root)
    maxSum = float('-inf')
    for level in range(height):
        levelSum = getMaxSum(root, level)
        maxSum = max(maxSum, levelSum)
    return maxSum

def isValidBST(root):
    def inorder(node, prev):
        if node is None:
            return True
        if not inorder(node.left, prev):
            return False
        if node.val <= prev[0]:
            return False
        prev[0] = node.val
        return inorder(node.right, prev)
    
    prev = [float('-inf')]
    return inorder(root, prev)