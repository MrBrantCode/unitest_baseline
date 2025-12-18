"""
QUESTION:
Implement a function called `search_word` that returns the index positions of each occurrence of a given word in a compressed trie data structure. The compressed trie should reduce redundant nodes by merging consecutive nodes with only one child. The function should start at the root node and compare the characters of the given word with the characters in the trie, utilizing a binary search approach to achieve a time complexity of O(log n). The function should return a list of index positions if the word is found, and an empty list otherwise.
"""

class CompressedTrieNode:
    def __init__(self, char):
        self.char = char
        self.index_positions = []
        self.children = {}

def search_word(root, word):
    node = root

    for char in word:
        if char in node.children:
            node = node.children[char]
        else:
            return []
    
    return node.index_positions