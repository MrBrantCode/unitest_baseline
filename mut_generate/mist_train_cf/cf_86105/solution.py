"""
QUESTION:
Generate a list of all possible unique character combinations from a given string, where the order of selection matters. The function should take two parameters: the input string and the maximum length of the combinations. The function should exclude combinations that repeat the same character and limit the maximum length of the combinations. 

The function should be named `combinations` and it should return a list of strings, where each string represents a unique combination of characters. 

The function should work with strings that contain both lowercase and uppercase letters as well as special characters.
"""

from itertools import permutations

def combinations(string, max_length):
    result = []
    for length in range(1, max_length + 1):
        result.extend(''.join(p) for p in permutations(string, length))
    return list(set(result))