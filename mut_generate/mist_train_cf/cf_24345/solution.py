"""
QUESTION:
Construct a function `insert` that constructs a binary search tree from a given array of integers. The `insert` function should take two parameters: the root of the tree and the data to be inserted. The function should create a new node if the tree is empty, and recursively insert the data into the left or right subtree based on the value comparison with the root.
"""

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def insert(root, data): 
    if root is None: 
        return Node(data) 
    else: 
        if root.data > data: 
            root.left = insert(root.left, data) 
        else: 
            root.right = insert(root.right, data) 
        return root 