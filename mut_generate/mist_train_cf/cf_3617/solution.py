"""
QUESTION:
Write a function `generate_permutations` that generates all permutations of a given string. The function should handle cases where the string contains duplicate characters and should only consider each unique permutation once. The input string length will not exceed 15 characters.
"""

def generate_permutations(string):
    permutations = []
    if len(string) == 0:
        permutations.append(string)
    else:
        for i in range(len(string)):
            if i > 0 and string[i] == string[i-1]:  # Skip duplicates
                continue
            first = string[i]
            remaining = string[:i] + string[i+1:]
            for sub_permutation in generate_permutations(remaining):
                permutations.append(first + sub_permutation)
    return permutations