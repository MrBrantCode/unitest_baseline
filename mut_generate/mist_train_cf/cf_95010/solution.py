"""
QUESTION:
Implement a function `count_word_occurrences(html)` that takes an HTML string as input, extracts the text content, and returns a dictionary or a sorted list of tuples containing each word and its occurrence count. The solution should handle cases where the HTML document contains nested tags and ignore HTML tags. The function should use a binary search tree to store the word occurrences in sorted order.
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
    return inorder_traversal(root)