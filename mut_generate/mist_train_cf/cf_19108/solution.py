"""
QUESTION:
Write a function named `generate_permutations` that generates all unique permutations of the characters in a given string without using recursion. The function should be able to handle input strings with duplicate characters and input strings of length up to 10^6 efficiently. The function should return a list of strings, each representing a unique permutation of the input string.
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