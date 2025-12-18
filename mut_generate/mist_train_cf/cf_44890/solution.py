"""
QUESTION:
Implement a function `kthSmallest(Tree, k)` that finds the kth smallest element in an AVL tree. The function should maintain an O(log n) time complexity and handle edge cases such as an empty tree. Each node in the AVL tree stores the size of its subtree, which is updated during insertion and deletion operations. The function should return the kth smallest element in the tree or an error message if the tree is empty.
"""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

def kthSmallest(root, k):
    """
    Finds the kth smallest element in an AVL tree.

    Args:
    root (TreeNode): The root of the AVL tree.
    k (int): The position of the element to be found.

    Returns:
    int: The kth smallest element in the tree, or "Tree is empty" if the tree is empty.
    """
    
    # Base case: If the tree is empty
    if root is None:
        return "Tree is empty"
    
    # Calculate the total number of nodes in the left subtree
    total = getSize(root.left) + 1
    
    # If k is equal to the total number of nodes in the left subtree and the root
    if k == total:
        return root.key
    
    # If k is less than the total number of nodes in the left subtree
    elif k < total:
        return kthSmallest(root.left, k)
    
    # If k is greater than the total number of nodes in the left subtree
    else:
        return kthSmallest(root.right, k - total)

def getSize(node):
    """
    Gets the size of a tree node.

    Args:
    node (TreeNode): The node whose size is to be retrieved.

    Returns:
    int: The size of the tree node, or 0 if the node is None.
    """
    return node.size if node else 0