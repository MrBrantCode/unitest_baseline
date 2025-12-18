"""
QUESTION:
Implement a function `kth_largest(root, k)` to find the kth largest node in a binary search tree (BST), where `root` is the root of the BST and `k` is the rank of the node to be found. The function should have a time complexity of O(h), where h is the height of the tree. The BST should be augmented with a size attribute for each node, representing the number of nodes in the subtree rooted at that node. The function should handle edge cases, including when k is larger than the number of nodes in the tree.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1 # init size of itself 

# function to update the size attribute 
def size(node):
    if node is None:
        return 0
    else:
        return node.size

# function to insert a new node with given key
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left  = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    node.size = size(node.left) + size(node.right) + 1 # update size
    return node

# function to find the k'th largest key
def kth_largest(node, k):
    if node is None:
        return None

    r = size(node.right) + 1;

    if r == k:
        return node
    elif r > k:
        return kth_largest(node.right, k)
    else:
        return kth_largest(node.left, k-r)