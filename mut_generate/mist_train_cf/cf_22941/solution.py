"""
QUESTION:
Write an algorithm to implement the `find_lca` function, which finds the least common ancestor of two given nodes in a binary search tree. The binary search tree has unique integer keys for each node, where the key of each node is greater than the keys of all nodes in its left subtree and less than the keys of all nodes in its right subtree. The function should take as input the root of the binary search tree and two nodes, `node1` and `node2`, and return their least common ancestor. You may assume that both `node1` and `node2` exist in the binary search tree.
"""

def find_lca(root, node1, node2):
    curr = root
    while curr:
        if node1.key < curr.key and node2.key < curr.key:
            curr = curr.left
        elif node1.key > curr.key and node2.key > curr.key:
            curr = curr.right
        else:
            return curr
    return None