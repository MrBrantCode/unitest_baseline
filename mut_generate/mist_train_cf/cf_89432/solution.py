"""
QUESTION:
Write a function `get_unique_permutations(string)` that generates all unique permutations of a given string, where each character can be repeated at most twice, and a unique permutation is a permutation that does not have any repeated characters. The function should return a list of strings.
"""

def get_unique_permutations(string):
    if len(string) <= 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        for perm in get_unique_permutations(string[:i] + string[i+1:]):
            if perm.count(string[i]) < 2:  
                permutations.append(string[i] + perm)
            elif perm.count(string[i]) == 1 and perm[-1] != string[i]:  
                permutations.append(string[i] + perm)
    return list(set(permutations))