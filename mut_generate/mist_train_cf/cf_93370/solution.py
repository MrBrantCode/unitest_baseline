"""
QUESTION:
Write a function `generate_permutations` that generates all possible permutations of a given string. The function should have a time complexity of O(n!), where n is the length of the string.
"""

def generate_permutations(s):
    if len(s) <= 1:
        return [s]
    permutations = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in generate_permutations(remaining):
            permutations.append(char + perm)
    return permutations