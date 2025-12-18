"""
QUESTION:
Given inorder and level-order traversals of a Binary Tree, construct the Binary Tree and return the root Node. 
Input:
First line consists of T test cases. First line of every test case consists of N, denoting number of elements is respective arrays. Second and third line consists of arrays containing Inorder and Level-order traversal respectively.
Output:
Single line output, print the preOrder traversal of array.
Constraints:
1<=T<=100
1<=N<=100
Example:
Input:
2
3
1 0 2 
0 1 2 
7
3 1 4 0 5 2 6 
0 1 2 3 4 5 6 
Output:
0 1 2
0 1 3 4 2 5 6
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_binary_tree(inorder, level_order):
    def build(ino, start, end, d):
        if start > end:
            return None
        if start == end:
            return Node(ino[start])
        idx = start
        for i in range(start + 1, end + 1):
            if d[ino[i]] < d[ino[idx]]:
                idx = i
        root = Node(ino[idx])
        root.left = build(ino, start, idx - 1, d)
        root.right = build(ino, idx + 1, end, d)
        return root

    n = len(inorder)
    d = {level_order[i]: i for i in range(n)}
    return build(inorder, 0, n - 1, d)