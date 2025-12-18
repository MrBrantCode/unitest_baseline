"""
QUESTION:
Implement a function `traverse_tree` that performs pre-order, in-order, and post-order traversal of a tree data structure. The function should visit the root node and its subtrees in the respective order for each traversal type.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traverse_tree(root):
    """
    Performs pre-order, in-order, and post-order traversal of a tree data structure.
    
    Args:
        root (TreeNode): The root node of the tree.
    
    Returns:
        tuple: A tuple containing the pre-order, in-order, and post-order traversal results.
    """
    
    def pre_order(root):
        """
        Performs pre-order traversal of a tree data structure.
        
        Args:
            root (TreeNode): The root node of the tree.
        
        Returns:
            list: A list of node values in pre-order.
        """
        if root is None:
            return []
        return [root.val] + pre_order(root.left) + pre_order(root.right)

    def in_order(root):
        """
        Performs in-order traversal of a tree data structure.
        
        Args:
            root (TreeNode): The root node of the tree.
        
        Returns:
            list: A list of node values in in-order.
        """
        if root is None:
            return []
        return in_order(root.left) + [root.val] + in_order(root.right)

    def post_order(root):
        """
        Performs post-order traversal of a tree data structure.
        
        Args:
            root (TreeNode): The root node of the tree.
        
        Returns:
            list: A list of node values in post-order.
        """
        if root is None:
            return []
        return post_order(root.left) + post_order(root.right) + [root.val]
    
    return (pre_order(root), in_order(root), post_order(root))