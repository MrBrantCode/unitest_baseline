"""
QUESTION:
Given postorder traversal of a Binary Search Tree, you need to construct a BST from postorder traversal. The output will be inorder traversal of the constructed BST.
 
Example 1:
Input:
6
1 7 5 50 40 10
Output:
1 5 7 10 40 50
Explanation:
Testcase 1: The BST for the given post order traversal is:
Thus the inorder traversal of BST is: 1 5 7 10 40 50.
 
Your Task:
The task is to complete the function constructTree() which takes an array post[], size as as the argument and returns the root of BST. 
 
Expected Time Complexity: O(No. of  nodes in BST)
Expected Auxiliary Space: O(No. of  nodes in BST)
 
Constraints:
1 <= T <= 100
1 <= N <= 200
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_bst_from_postorder(postorder):
    if not postorder:
        return None
    
    node_val = postorder.pop()
    root = Node(node_val)
    
    i = len(postorder) - 1
    while i >= 0:
        if postorder[i] > node_val:
            i -= 1
        else:
            break
    
    root.right = construct_bst_from_postorder(postorder[i + 1:])
    root.left = construct_bst_from_postorder(postorder[:i + 1])
    
    return root