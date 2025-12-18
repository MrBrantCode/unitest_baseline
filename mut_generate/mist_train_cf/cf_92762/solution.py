"""
QUESTION:
Write a function `get_permutations(string)` that generates all unique permutations of the input string. The function should be able to handle empty strings. The function should return a list of strings where each string is a permutation of the input string.
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