"""
QUESTION:
Implement the function `isValidSerialization(preorder)` that takes a string of comma-separated values as input, representing a preorder traversal of a binary tree where `#` represents a null node. Return `true` if the string is a valid preorder serialization of a binary tree and `false` otherwise. The function should not reconstruct the tree and should handle strings with leading or trailing spaces, and integers with leading zeros. The length of the input string is guaranteed to be between 1 and 10^4, and the string consists of integers in the range [0, 100] and `#` separated by commas.
"""

def isValidSerialization(preorder):
    nodes = preorder.strip().split(',')
    diff = 1  
    for node in nodes:
        diff -= 1  
        if diff < 0:  
            return False
        if node != '#':  
            diff += 2
    return diff == 0  