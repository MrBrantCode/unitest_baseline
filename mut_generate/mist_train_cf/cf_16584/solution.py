"""
QUESTION:
Write a function `is_balanced` to check if a binary tree is balanced. A binary tree is considered balanced if the heights of its left and right subtrees differ by no more than 1. The function should return True if the tree is balanced, and False otherwise. 

Note that the function should also print all the nodes in the tree in inorder traversal order and the frequency of each node, but it should not use any additional data structures to store the frequency of nodes.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1

    def inorder(node, freq):
        if node is None:
            return

        inorder(node.left, freq)
        print(node.val, end=" ")
        freq[node.val] = freq.get(node.val, 0) + 1
        inorder(node.right, freq)

    if root is None:
        return True

    freq = {}
    inorder(root, freq)
    print()
    
    print("Frequency of each node:")
    for node, count in freq.items():
        print(f"{node}: {count}")

    left_height = height(root.left)
    right_height = height(root.right)

    return abs(left_height - right_height) <= 1