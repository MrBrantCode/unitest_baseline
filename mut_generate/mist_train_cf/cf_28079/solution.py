"""
QUESTION:
Implement a `Trie` class with the `add(word)` and `search(word)` methods. The `add(word)` method should add the given word to the Trie, and the `search(word)` method should return `True` if the word is in the Trie, and `False` otherwise. 

Restrictions: 
- Each node in the Trie represents a single character of the string.
- The root node is empty, and each subsequent level represents one character of the string.
- The path from the root to a particular node spells out a word.
- Each node may have multiple children, each representing a different character.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def entrance(word, action, trie=None):
    if trie is None:
        trie = TrieNode()
    if action == "add":
        node = trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    elif action == "search":
        node = trie
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    return trie