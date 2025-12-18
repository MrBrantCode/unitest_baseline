"""
QUESTION:
Given an array representing a binary tree where each node's left child is at index 2*i + 1 and right child at 2*i + 2, determine if it is a valid binary search tree (BST) with the possibility of duplicate values. Create a function `isValidBST` that takes in the array and returns True if it represents a valid BST and False otherwise.
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