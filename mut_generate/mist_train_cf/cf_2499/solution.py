"""
QUESTION:
Convert a binary search tree to a sorted array using a time complexity of O(n) and a constant amount of extra space (excluding the input tree and the output array). The solution should handle duplicate values in the tree and maintain the sorted order of elements in the resulting array. Do not use built-in sorting functions or data structures.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def treeToSortedList(root):
    prev = None
    head = None
    result = []
    
    def treeToSortedListHelper(node):
        nonlocal prev, head, result
        if node is None:
            return
        
        treeToSortedListHelper(node.left)

        if prev is None:
            head = node
        else:
            prev.right = node
            node.left = prev

        prev = node
        result.append(node.value)

        treeToSortedListHelper(node.right)

    treeToSortedListHelper(root)
    return result