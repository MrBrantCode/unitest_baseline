"""
QUESTION:
Write a function `count_greater` that, given the root of a binary search tree (BST), returns a list where the i-th element represents the number of values greater than the i-th node in the BST. The function should have a time complexity of O(n), where n is the number of nodes in the BST.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_greater(root):
    count_list = []
    
    def count_greater_helper(node):
        if node is None:
            return 0
        
        right_count = count_greater_helper(node.right)
        left_count = count_greater_helper(node.left)
        
        count = right_count + left_count + 1
        count_list.append(count)
        
        return count
    
    count_greater_helper(root)
    return count_list