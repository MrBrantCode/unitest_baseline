"""
QUESTION:
Implement a data structure that can store a large dictionary of words and their meanings, allowing for fast retrieval of both words and meanings, while limiting memory usage to under 50 MB. The solution should also efficiently handle frequent updates to the dictionary. The data structure should have an average time complexity of O(1) for retrieval and support efficient insertion and deletion of words.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Dictionary:
    def __init__(self):
        self.root = TrieNode()
        self.hash_table = {}

    def insert(self, word, meaning):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        self.hash_table[word] = meaning

    def get(self, word):
        if word in self.hash_table:
            return self.hash_table[word]
        return None

    def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                if not node.end_of_word:
                    return False
                node.end_of_word = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            should_delete_current_node = _delete(node.children[char], word, index + 1)
            if should_delete_current_node:
                del node.children[char]
                return len(node.children) == 0
            return False

        _delete(self.root, word, 0)
        if word in self.hash_table:
            del self.hash_table[word]

def entrance(word, meaning=None):
    dictionary = Dictionary()
    if meaning:
        dictionary.insert(word, meaning)
    else:
        return dictionary.get(word)