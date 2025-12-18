"""
QUESTION:
Design a function called `isValidEnglishWord` that determines if a given string is a valid English word or not, considering the following requirements:

- The function should use a Trie data structure to efficiently store and retrieve words.
- The function should be case-insensitive, meaning that it should consider "Construct" and "construct" as the same word.
- The function should handle special characters and numbers in the input string, treating them as invalid characters.
- The function should have a time complexity of O(n), where n is the length of the input string.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            char = char.lower()
            if char.isalpha():
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            char = char.lower()
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word


def isValidEnglishWord(word, dictionary):
    trie = Trie()
    # Load dictionary words into the Trie
    for dict_word in dictionary:
        trie.insert(dict_word)

    # Check if the given word is in the Trie
    return trie.search(word.lower())