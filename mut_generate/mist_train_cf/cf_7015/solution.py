"""
QUESTION:
Create a function called `isValidEnglishWord` that determines if a given string is a valid English word or not. The function should have a time complexity of O(n), where n is the length of the input string, and use a Trie data structure to efficiently store and retrieve words. The function should be case-insensitive and handle special characters and numbers in the input string as invalid characters.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

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


def isValidEnglishWord(words, word):
    """
    Checks if a given word is a valid English word.

    Args:
    words (list): A list of valid English words.
    word (str): The word to be checked.

    Returns:
    bool: True if the word is valid, False otherwise.
    """
    trie = Trie(words)
    return trie.search(word)