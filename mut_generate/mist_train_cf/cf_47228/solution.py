"""
QUESTION:
Write a function named `minimumLengthEncoding` that takes a list of strings `words` as input, where `1 <= len(words) <= 2000` and `1 <= len(words[i]) <= 7`. Each string consists of only lowercase letters and no word is a prefix of another word in the `words` array. Return the length of the shortest reference string `s` possible of any valid encoding of `words`. The reference string `s` ends with the `'#'` character and for each index `i`, the substring of `s` starting from `i` and up to (but not including) the next `'#'` character is equal to `words[i]`.
"""

def minimumLengthEncoding(words):
    root = dict()
    leaves = []
    # construct the trie.
    for word in set(words):
        node = root
        for letter in reversed(word):
            node[letter] = node = node.get(letter, {})
        leaves.append((node, len(word) + 1))

    # we only add the length of the word for the ones
    # that have no children (i.e., their Character -> Dict is empty)
    return sum(depth for node, depth in leaves if len(node) == 0)