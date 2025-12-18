"""
QUESTION:
Develop an algorithm that finds all pairs of anagrams in a given list of strings. The function, `find_anagram_pairs(strings)`, should consider all possible combinations of strings and return a list of tuples containing the pairs of anagrams. The function should be able to handle large lists of strings with varying lengths.
"""

from collections import defaultdict
def find_anagram_pairs(strings):
    sorted_strings = defaultdict(list)
    for s in strings:
        sorted_strings[''.join(sorted(s))].append(s)
    anagram_pairs = []
    for key in sorted_strings:
        if len(sorted_strings[key]) > 1:
            for i in range(len(sorted_strings[key])):
                for j in range(i+1, len(sorted_strings[key])):
                    anagram_pairs.append((sorted_strings[key][i], sorted_strings[key][j]))
    return anagram_pairs