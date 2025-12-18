"""
QUESTION:
You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree.
You just have to complete the function.

Input Format

You are given a function,

Node * insert (Node * root ,int data) {

}

Constraints

No. of nodes in the  tree $\leq$ 500

Output Format

Return the root of the binary search tree after inserting the value into the tree.

Sample Input
        4
       / \
      2   7
     / \
    1   3

The value to be inserted is 6.

Sample Output
         4
       /   \
      2     7
     / \   /
    1   3 6
"""

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

def insert_into_bst(root, data):
    if root is None:
        return Node(data)
    else:
        if data <= root.info:
            root.left = insert_into_bst(root.left, data)
        else:
            root.right = insert_into_bst(root.right, data)
        return root