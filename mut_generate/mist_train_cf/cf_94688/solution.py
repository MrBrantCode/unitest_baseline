"""
QUESTION:
Write a function `convertBSTToArray` that takes the root of a binary search tree as input and returns a sorted array of the tree's node values. The function should handle duplicate values and maintain the sorted order of elements in the resulting array. The function should use a constant amount of extra space (excluding the input tree and the output array) and have a time complexity of O(n), where n is the number of nodes in the tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def convertBSTToArray(root):
    result = []
    stack = []
    current = root
    
    while current is not None or len(stack) > 0:
        while current is not None:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        
        current = current.right
    
    return result