"""
QUESTION:
Write a function `generate_permutations(string)` that generates all unique permutations of a given string without using recursion. The input string can contain duplicate characters. The function should handle these duplicates correctly and be able to handle input strings of length up to 10^6 efficiently.
"""

from collections import Counter

def generate_permutations(string):
    result = []
    counter = Counter(string)
    unique_chars = list(counter.keys())
    counts = list(counter.values())
    current = [''] * len(string)

    def permute_helper(level):
        if level == len(current):
            result.append(''.join(current))
            return

        for i in range(len(unique_chars)):
            if counts[i] == 0:
                continue
            current[level] = unique_chars[i]
            counts[i] -= 1
            permute_helper(level + 1)
            counts[i] += 1

    permute_helper(0)
    return result