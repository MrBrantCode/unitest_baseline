"""
QUESTION:
Implement a function called `count_word_occurrences(html)` that takes an HTML string as input, extracts the text content, counts the occurrences of each word, and stores them in a binary search tree in sorted order. The function should handle cases with nested HTML tags and ignore the tags themselves.
"""

import re

class Node:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.left = None
        self.right = None

def insert(root, word):
    if root is None:
        return Node(word)
    if word < root.word:
        root.left = insert(root.left, word)
    elif word > root.word:
        root.right = insert(root.right, word)
    else:
        root.count += 1
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.word, root.count)
        inorder_traversal(root.right)

def count_word_occurrences(html):
    text = re.sub(r'<[^>]+>', '', html)  # Remove HTML tags
    words = re.findall(r'\w+', text.lower())  # Split text into words
    root = None
    for word in words:
        root = insert(root, word)
    inorder_traversal(root)