"""
QUESTION:
Write a function `generate_permutations(s)` that generates all unique permutations of a given string `s`. The function should return a list of all possible permutations.
"""

def generate_permutations(s):
    results = []
    if len(s) == 1:
        results.append(s)
    else:
        for i, c in enumerate(s):
            for perm in generate_permutations(s[:i] + s[i + 1:]):
                results.append(c + perm)
    return results