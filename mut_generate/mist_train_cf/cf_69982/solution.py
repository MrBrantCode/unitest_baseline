"""
QUESTION:
Write a function `max_unique_substrings` that takes a string `s` of digits from '1' to '9' as input and returns the maximum number of unique substrings that can be generated from `s`. The length of `s` is guaranteed to be between 1 and 10^5. The function should be able to handle cases where `s` contains duplicate digits and is not sorted in any particular order.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfString = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endOfString

def max_unique_substrings(s):
    """
    This function takes a string s of digits from '1' to '9' as input and returns 
    the maximum number of unique substrings that can be generated from s.
    
    Parameters:
    s (str): The input string of digits from '1' to '9'.
    
    Returns:
    int: The maximum number of unique substrings that can be generated from s.
    """
    trie = Trie()
    max_unique = 0
    for length in range(1, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if not trie.search(substring):
                trie.insert(substring)
                max_unique += 1
    return max_unique