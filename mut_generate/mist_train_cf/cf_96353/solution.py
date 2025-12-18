"""
QUESTION:
Implement a function named `bfs_traversal` that performs a breadth-first search traversal on a binary tree and prints the values of the nodes in the order they are visited. The function should not use any built-in Python libraries or data structures for queue operations. The binary tree is represented using a `Node` class with `value`, `left`, and `right` attributes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_traversal(root):
    if root is None:
        return

    queue = [root]  

    while queue:
        node = queue.pop(0)  
        print(node.value)  

        if node.left:  
            queue.append(node.left)

        if node.right:  
            queue.append(node.right)