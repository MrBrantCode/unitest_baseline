"""
QUESTION:
Write a function named `is_valid_word` that determines if a given string is a valid English word or not. The function should have a time complexity of O(n), where n is the length of the input string. It should use a Trie data structure to efficiently store and retrieve words, be case-insensitive, handle special characters and numbers as invalid characters, and not rely on any external libraries or dictionaries for word validation. The function will be provided with a list of valid English words to populate the Trie.
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

def is_valid_word(valid_words, word):
    trie = Trie()
    for valid_word in valid_words:
        trie.insert(valid_word.lower())  

    word = ''.join(c for c in word if c.isalpha())

    return trie.search(word.lower())