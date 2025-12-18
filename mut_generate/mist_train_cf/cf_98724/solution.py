"""
QUESTION:
Design a comprehensive algorithmic approach for implementing and evaluating common data structures such as stacks, queues, linked lists, and binary trees.

The approach should consider the following factors when selecting a data structure: 
- Purpose: The data structure's suitability for the task.
- Data size: The size of the data that needs to be stored.
- Access and insertion time: The time it takes to access or insert data.
- Memory usage: The amount of memory required by the data structure.
- Ordering of data: The way data is ordered.

The implementation should aim to minimize time and space complexity, avoid unnecessary memory allocation, and use caching to store frequently accessed data.

The approach should also include a plan to evaluate the strengths and limitations of the chosen data structure under various scenarios, including different data sizes, user interactions, and real-time constraints.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def entance(root, key):
    """
    Adds a new node to the binary search tree.

    Args:
        root (Node): The root of the binary search tree.
        key (int): The value of the new node.

    Returns:
        Node: The root of the updated binary search tree.
    """
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = entance(root.left, key)
    else:
        root.right = entance(root.right, key)

    return root

def inorder_traversal(root):
    """
    Prints the values of the binary search tree in ascending order.

    Args:
        root (Node): The root of the binary search tree.
    """
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

# Example usage:
root = None
root = entance(root, 50)
root = entance(root, 30)
root = entance(root, 20)
root = entance(root, 40)
root = entance(root, 70)
root = entance(root, 60)
root = entance(root, 80)

inorder_traversal(root)  # Output: 20 30 40 50 60 70 80