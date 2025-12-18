"""
QUESTION:
Implement the `word_frequency` function, which takes a sentence as input and returns a dictionary with word frequencies, excluding common stop words ("the", "is", "and") and punctuation, and treating words as case-insensitive.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0

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
        current.frequency += 1

def word_frequency(sentence):
    stop_words = {"the", "is", "and"}  # common stop words to exclude
    trie = Trie()

    # Preprocess the sentence by removing punctuation and converting to lowercase
    sentence = ''.join(ch.lower() for ch in sentence if ch.isalnum() or ch.isspace())
    
    words = sentence.split()

    for word in words:
        if word not in stop_words:
            trie.insert(word)

    return get_word_frequency(trie.root, '')

def get_word_frequency(node, prefix):
    frequency_dict = {}
    
    if node.is_end_of_word:
        frequency_dict[prefix] = node.frequency

    for char, child in node.children.items():
        frequency_dict.update(get_word_frequency(child, prefix + char))
    
    return frequency_dict