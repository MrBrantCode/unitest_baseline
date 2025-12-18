"""
QUESTION:
Write a function named `get_permutations` that returns all permutations of a given string. The function should be able to handle strings of any length, including empty strings. The function should return a list of all possible permutations, where each permutation is a string.
"""

def get_permutations(string):
    if len(string) == 0:
        return []
    
    if len(string) == 1:
        return [string]
    
    permutations = []
    for i in range(len(string)):
        for perm in get_permutations(string[:i] + string[i+1:]):
            permutations.append(string[i] + perm)
    return permutations