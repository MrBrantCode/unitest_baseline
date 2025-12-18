"""
QUESTION:
Write a function named `find_combinations` that generates all unique combinations of letters from a given string, ignoring the order of characters and handling repeating characters. The function should be efficient for strings with more than 20 characters. Consider the time and space complexity of the algorithm.
"""

from itertools import combinations

def find_combinations(string: str):
    res = set()
    for comb_len in range(1, len(string) + 1):
        for subset in combinations(string, comb_len):
            res.add("".join(sorted(subset)))
    return res