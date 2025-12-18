"""
QUESTION:
Write a function `generate_permutations(string)` that takes a string as input and returns all permutations of the string. The function should return a list of all possible permutations.
"""

def generate_permutations(string):
    if len(string) == 1:
        return [string]

    all_perms = []
    for i, c in enumerate(string):
        other_chars = string[:i] + string[i+1:]
        other_perms = generate_permutations(other_chars)
        for perm in other_perms:
            all_perms.append(c + perm)
    return all_perms