"""
QUESTION:
Implement the `makeTrie` function to construct a trie from a list of words, and the `r_trie` function to return a reversed trie where each word is reversed. The `makeTrie` function should take a list of words as input and return the root of the constructed trie. The `r_trie` function should take the root of the original trie as input and return the root of the reversed trie. Use the provided TrieNode class to represent the nodes of the trie. The TrieNode class has a `children` dictionary to store the child nodes and an `is_end_of_word` boolean to mark the end of a word.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def makeTrie(words):
    root = TrieNode()
    for word in words:
        current = root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    return root