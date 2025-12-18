"""
QUESTION:
Given an array of integers in[] representing inorder traversal of elements of a binary tree. Return true if the given inorder traversal can be of a valid Binary Search Tree.
Note - All the keys in BST must be unique
 
Example 1:
Input: in = [8, 14, 45, 64, 100]
Output: True
Example 2:
Input: in[] = [5, 6, 1, 8, 7]
Output: False
 
Your Task:
Complete the function isBSTTraversal() which takes an integer array in[] as input and return true if the traversal represents a BST.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
 
Constraints:
1<=n<=10^{5}
1<=in[i]<=10^{9}
"""

def is_valid_bst_inorder(inorder_traversal):
    """
    Determines if the given inorder traversal can represent a valid Binary Search Tree (BST).

    Parameters:
    inorder_traversal (list of int): The inorder traversal of the binary tree.

    Returns:
    bool: True if the traversal represents a valid BST, otherwise False.
    """
    for idx in range(1, len(inorder_traversal)):
        if inorder_traversal[idx - 1] >= inorder_traversal[idx]:
            return False
    return True