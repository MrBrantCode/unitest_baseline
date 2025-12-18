"""
QUESTION:
Write a function `get_unique_permutations` that generates all unique permutations of a given string where each character can be repeated at most twice. A unique permutation is a permutation that does not have any repeated characters in different positions, but the same character can appear up to two times in a permutation.
"""

def get_unique_permutations(string):
    if len(string) <= 1:
        return [string]

    permutations = set()
    for i in range(len(string)):
        for perm in get_unique_permutations(string[:i] + string[i+1:]):
            if perm.count(string[i]) < 2:  
                permutations.add(string[i] + perm)
            elif perm.count(string[i]) == 1 and perm[-1] != string[i]:  
                permutations.add(string[i] + perm)
    return list(permutations)