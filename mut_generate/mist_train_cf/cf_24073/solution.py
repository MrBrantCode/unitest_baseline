"""
QUESTION:
Write a function called `tree_to_array` to convert a binary search tree into a sorted array using an inorder traversal, resulting in an array containing the elements in ascending order. The function should have a time complexity of O(n), where n is the number of nodes in the tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_to_array(root):
    """
    This function converts a binary search tree into a sorted array using an inorder traversal.
    
    Args:
        root (TreeNode): The root node of the binary search tree.
    
    Returns:
        list: A sorted array containing the elements in ascending order.
    """
    result = []
    
    def inorder_traversal(node):
        # Traverse the left subtree
        if node and node.left:
            inorder_traversal(node.left)
        
        # Visit the current node
        if node:
            result.append(node.val)
        
        # Traverse the right subtree
        if node and node.right:
            inorder_traversal(node.right)
    
    # Start the traversal from the root node
    inorder_traversal(root)
    
    return result