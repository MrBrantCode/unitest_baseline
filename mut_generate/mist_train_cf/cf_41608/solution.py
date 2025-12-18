"""
QUESTION:
Write a function `longest_anagram_group(words)` that takes a list of words as input and returns the longest anagram group. If there are multiple anagram groups of the same maximum length, return the one that appears first in the input list.
"""

def longest_anagram_group(words):
    anagram_groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    max_length = 0
    longest_group = []
    for group in anagram_groups.values():
        if len(group) > max_length:
            max_length = len(group)
            longest_group = group

    return longest_group