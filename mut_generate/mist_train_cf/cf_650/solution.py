"""
QUESTION:
Implement a function `getWordsStartingWith(letter: str, dictionary: List[str]) -> List[str]` that takes a letter and a list of words and returns a list of all words that start with the given letter. The function should allow for fast retrieval of words and have a time complexity of O(n) or better for the retrieval operation and a space complexity of O(n) where n is the number of words in the dictionary.
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

    def _getAllWords(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self._getAllWords(child, prefix + char))
        return words

def entance(letter, dictionary):
    trie = Trie()
    for word in dictionary:
        trie.insert(word.lower())  # Convert all words to lowercase for case-insensitive search
    node = trie.root
    for char in letter:
        if char not in node.children:
            return []
        node = node.children[char]
    return trie._getAllWords(node, letter.lower())  # Convert the letter to lowercase as well