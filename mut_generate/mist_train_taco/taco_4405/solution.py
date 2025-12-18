"""
QUESTION:
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix).
It will return the word with given prefix and suffix with maximum weight.  If no word exists, return -1.


Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1


Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
"""

def find_max_weight_word(words, prefix, suffix):
    max_weight = -1
    
    for i, word in enumerate(words):
        if word.startswith(prefix) and word.endswith(suffix):
            max_weight = max(max_weight, i)
    
    return max_weight