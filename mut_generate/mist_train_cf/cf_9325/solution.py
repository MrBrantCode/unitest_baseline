"""
QUESTION:
Given an array representing the nodes of a binary tree, where each node has a unique index and a value, determine if the array represents a valid binary search tree (BST) and write a function `isValidBST(arr)` that returns a boolean indicating whether the array is a valid BST or not. The array can contain duplicates. The function should only take the array `arr` as an input parameter and the array indices are assumed to be the in-order traversal of the binary tree, where for any given node at position `i`, the left child is at position `2*i + 1` and the right child is at position `2*i + 2`.
"""

def isValidBST(arr):
    def helper(idx, minVal, maxVal):
        if idx >= len(arr):
            return True

        value = arr[idx]
        if value <= minVal or value >= maxVal:
            return False

        if not helper(idx * 2 + 1, minVal, value):
            return False

        if not helper(idx * 2 + 2, value, maxVal):
            return False

        return True

    return helper(0, float('-inf'), float('inf'))