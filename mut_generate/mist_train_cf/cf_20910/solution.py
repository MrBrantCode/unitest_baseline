"""
QUESTION:
Implement a function named `bfs_traversal` that takes the root node of a binary tree as input and performs a breadth-first search (BFS) traversal. The function should process each node in the tree without using any built-in Python libraries or data structures for queue operations. The binary tree is represented using a `Node` class with attributes `value`, `left`, and `right`. Provide the time and space complexity of the implementation.
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