"""
QUESTION:
Design a function called `search_thesaurus` to efficiently search through a digital thesaurus. The function should return relevant words from the thesaurus based on a given input. The function should be able to handle large datasets and various semantic relationships between words.
"""

class TrieNode:
    """A node in the trie data structure."""
    
    def __init__(self):
        # Initialize an empty node with an empty dictionary to store children
        self.children = {}
        # Initialize an empty list to store synonyms
        self.synonyms = []

class Thesaurus:
    """A digital thesaurus implemented using a trie data structure."""
    
    def __init__(self):
        # Initialize the thesaurus with a root node
        self.root = TrieNode()

    def insert(self, word, synonyms):
        """Insert a word and its synonyms into the thesaurus."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.synonyms = synonyms

    def search(self, word):
        """Search for a word in the thesaurus and return its synonyms."""
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.synonyms

def search_thesaurus(thesaurus, word):
    """Search for a word in the thesaurus and return its synonyms."""
    return thesaurus.search(word)

# Example usage:
thesaurus = Thesaurus()
thesaurus.insert("big", ["large", "huge", "enormous"])
thesaurus.insert("small", ["little", "tiny", "miniature"])

print(search_thesaurus(thesaurus, "big"))  # Output: ["large", "huge", "enormous"]
print(search_thesaurus(thesaurus, "small"))  # Output: ["little", "tiny", "miniature"]