"""
QUESTION:
Construct the binary tree from a string and validate if it is a Binary Search Tree (BST). The input string consists of parentheses and integers, where an integer represents the root's value and a pair of parentheses contains a child binary tree with the same structure.

The function should be named `construct_and_validate` and should take a string `s` as input, where `0 <= s.length <= 3 * 10^4` and `s` consists of digits, `'('`, `')'`, and `'-'` only. The function should return a list of the tree's node values and a boolean indicating whether the tree is a valid BST.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_and_validate(s):
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
            root.left = construct_tree(s[start:i-1])
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
            root.right = construct_tree(s[start:i-1])
        return root

    def is_BST(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        if not min_val < node.val < max_val:
            return False
        return is_BST(node.left, min_val, node.val) and is_BST(node.right, node.val, max_val)

    tree = construct_tree(s)
    return [node.val for node in traverse(tree)], is_BST(tree)

def traverse(node):
    if node is None:
        return []
    return [node] + traverse(node.left) + traverse(node.right)