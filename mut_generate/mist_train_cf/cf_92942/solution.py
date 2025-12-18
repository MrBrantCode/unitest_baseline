"""
QUESTION:
Implement the `is_valid_word` function, which determines if a given string is a valid English word. The function should have a time complexity of O(n), where n is the length of the input string, and use a Trie data structure to store and retrieve words. The function should be case-insensitive, handle special characters and numbers as invalid characters, and not rely on any external libraries or dictionaries for word validation.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def is_valid_word(word):
    trie = Trie()
    valid_words = ["apple", "banana", "cherry", "durian", "elderberry"]
    for valid_word in valid_words:
        trie.insert(valid_word.lower())  

    word = ''.join(c for c in word if c.isalpha())

    return trie.search(word.lower())