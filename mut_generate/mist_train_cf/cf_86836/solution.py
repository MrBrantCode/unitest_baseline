"""
QUESTION:
Develop a function `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix string among all the strings in the list. The function should consider case sensitivity and handle any character encoding, including Unicode. The input list can contain up to 10^6 strings, each with a maximum length of 10^4 characters. The function should achieve a time complexity of O(N*M) and a space complexity of O(M), where N is the length of the list of strings and M is the maximum length of the strings.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

def longest_common_prefix(strings):
    """
    This function takes a list of strings as input and returns the longest common prefix string among all the strings in the list.

    Args:
        strings (list): A list of strings.

    Returns:
        str: The longest common prefix string.
    """
    if not strings:
        return ""

    # Initialize a TrieNode
    node = TrieNode()

    # Insert all strings into the Trie
    for string in strings:
        temp_node = node
        for char in string:
            if char not in temp_node.children:
                temp_node.children[char] = TrieNode()
            temp_node = temp_node.children[char]

    # Find the longest common prefix
    prefix = ""
    temp_node = node
    while len(temp_node.children) == 1 and not temp_node.is_word:
        char = list(temp_node.children.keys())[0]
        prefix += char
        temp_node = temp_node.children[char]

    return prefix