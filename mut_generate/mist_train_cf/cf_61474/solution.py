"""
QUESTION:
Construct a Binary Search Tree from a String and Validate it

Create three functions: `TreeNode`, `construct_tree(s)`, and `is_BST(node, min_val, max_val)`. 

The `TreeNode` function should initialize a tree node with a given value. 

The `construct_tree(s)` function should construct a binary search tree from a given string `s` representing a tree in pre-order traversal, where a node's value is followed by its left and right children in parentheses. The function should return the root node of the constructed tree. If the construction is not possible, the function should return `None`. 

The `is_BST(node, min_val, max_val)` function should check if a given binary tree rooted at `node` is a binary search tree. 

The `construct_and_validate(s)` function should construct a binary search tree from a given string `s` and validate if the constructed tree is a binary search tree. 

Restrictions: 
- The input string `s` is a valid pre-order traversal of a binary tree.
- The values of the tree nodes are integers.
- The tree is represented in the format `val(L)(R)`, where `val` is the node's value, and `L` and `R` are the left and right sub-trees, respectively.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct_tree(s):
    if not s:
        return None
    root_val = ""
    i = 0
    while i < len(s) and (s[i] == '-' or s[i].isdigit()):
        root_val += s[i]
        i += 1
    root = TreeNode(int(root_val))
    if i < len(s) and s[i] == '(':
        i += 1
        count = 1
        start = i
        while i < len(s) and count > 0:
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            i += 1
        root.left = construct_tree(s[start:i])
        if i < len(s) and s[i] == '(':
            i += 1
            count = 1
            start = i
            while i < len(s) and count > 0:
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                i += 1
            root.right = construct_tree(s[start:i])
    return root


def is_BST(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    if not min_val < node.val < max_val:
        return False
    return is_BST(node.left, min_val, node.val) and is_BST(node.right, node.val, max_val)


def construct_and_validate(s):
    tree = construct_tree(s)
    return is_BST(tree)