"""
QUESTION:
Implement a `buildFileIndex` function that takes a list of unique file paths as input and returns a `FileIndex` object. The `FileIndex` object should have a `searchFiles` method that takes a query string as input and returns a list of file paths that match the query. The query can be a partial or complete file path. The file paths are represented as strings and may contain alphanumeric characters, slashes, and periods. 

The `FileIndex` object should be implemented using a data structure that efficiently stores and retrieves file paths. The `searchFiles` method should use this data structure to efficiently search for files matching the given query.
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def _dfs(self, node: TrieNode, prefix: str) -> List[str]:
        result = []
        if node.is_end_of_word:
            result.append(prefix)
        for char, child in node.children.items():
            result.extend(self._dfs(child, prefix + char))
        return result

def buildFileIndex(file_paths: List[str]):
    trie = Trie()
    for file_path in file_paths:
        trie.insert(file_path)

    class FileIndex:
        def __init__(self, trie):
            self.trie = trie

        def searchFiles(self, query: str) -> List[str]:
            node = self.trie.root
            for char in query:
                if char not in node.children:
                    return []
                node = node.children[char]
            return self.trie._dfs(node, query)

    return FileIndex(trie)