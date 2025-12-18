"""
QUESTION:
Implement the function `minimumLengthEncoding` that takes an array of words as input and returns the length of the most compact reference sequence feasible for any legitimate representation of the words.

The words array `words` has the following restrictions:
- 1 <= len(words) <= 2000
- 1 <= len(words[i]) <= 7
- words[i] is composed of only lowercase alphabets.

The function should return the length of the most compact reference sequence s, which is the sum of the lengths of the words in the sequence plus the number of words, where the sequence is formed by selecting the words in such a way that any word that is a suffix of another word is ignored.
"""

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '#'

    def insert(self, word):
        is_new_word = False
        node = self.root
        for i in range(len(word) - 1, -1, -1):
            if word[i] not in node:
                is_new_word = True
                node[word[i]] = {}
            node = node[word[i]]
        if self.end_symbol not in node:
            node[self.end_symbol] = {}
            is_new_word = True
        return is_new_word

def minimumLengthEncoding(words):
    trie = Trie()
    words.sort(key = lambda word: [ -len(word), word])
    return sum(len(word) + 1 for word in words if trie.insert(word))