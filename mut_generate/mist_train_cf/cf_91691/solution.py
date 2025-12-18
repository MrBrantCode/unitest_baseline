"""
QUESTION:
Write a function `get_permutations(s)` that generates all possible permutations of the input string `s` without using any built-in permutation functions. The function should have a time complexity of less than O(n!), where n is the length of `s`.
"""

def get_permutations(s):
    if len(s) <= 1:
        return [s]
    
    permutations = []
    sub_permutations = get_permutations(s[1:])
    
    for sub_permutation in sub_permutations:
        for i in range(len(sub_permutation) + 1):
            permutations.append(sub_permutation[:i] + s[0] + sub_permutation[i:])
    
    return permutations