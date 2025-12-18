"""
QUESTION:
Implement a function named `build_dictionary` to store a dictionary of English words efficiently in terms of time and space complexity, allowing for fast retrieval of all words starting with a specific letter. The function should have a time complexity of O(n) for building the dictionary and O(k) for searching words, where n is the total number of characters in all words and k is the average length of words starting with the specified letter. The space complexity should be relatively low and related to the number of unique characters in the words.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def get_words(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        return self._get_words_from(current, prefix)

    def _get_words_from(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._get_words_from(child_node, prefix + char))
        return words

def build_dictionary(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie