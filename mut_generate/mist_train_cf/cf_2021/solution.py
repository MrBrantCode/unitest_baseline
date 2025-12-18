"""
QUESTION:
Create a function `unique_combinations` that takes a string of characters as an argument and returns a list of all unique combinations of characters possible, excluding any combination that includes a repeating character. The function should have a time complexity of O(n!), where n is the length of the input string.
"""

import itertools

def unique_combinations(string):
    result = []
    for r in range(1, len(string) + 1):
        combinations = list(itertools.combinations(string, r))
        for combo in combinations:
            if len(set(combo)) == len(combo):
                result.append(''.join(combo))
    return result