"""
QUESTION:
Implement a function `find_patterns(text: str, patterns: List[str]) -> List[List[int]]` that takes a text string and a list of patterns as input and returns a list of lists, where each inner list contains the starting positions of occurrences of a pattern within the text. The starting positions should be 0-indexed. The implementation should efficiently handle large texts and a large number of patterns.
"""

from typing import List

def find_patterns(text: str, patterns: List[str]) -> List[List[int]]:
    def build_trie(patterns):
        trie = {}
        node_count = 0
        for pattern in patterns:
            current_node = 0
            for char in pattern:
                if (current_node, char) not in trie:
                    node_count += 1
                    trie[(current_node, char)] = node_count
                current_node = trie[(current_node, char)]
        return trie

    def prefix_trie_matching(text, trie):
        index = 0
        symbol = text[index]
        v = 0
        while True:
            if not trie.get((v, symbol), None):
                return True
            elif trie.get((v, symbol), None) in trie.values():
                v = trie[(v, symbol)]
                index += 1
                if index < len(text):
                    symbol = text[index]
                else:
                    symbol = ''
            else:
                return False

    trie = build_trie(patterns)
    positions = []
    for i in range(len(text)):
        if prefix_trie_matching(text[i:], trie):
            positions.append(i)
    result = [[] for _ in range(len(patterns))]
    for i, pattern in enumerate(patterns):
        for position in positions:
            if text[position:position + len(pattern)] == pattern:
                result[i].append(position)
    return result