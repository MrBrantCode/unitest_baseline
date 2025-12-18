"""
QUESTION:
Write a function named `permutations` that takes a string as input and returns all possible permutations of that string. The function should be implemented using recursion. Note that if the input string contains duplicate characters, the function should return duplicate permutations.
"""

def permutations(string):
    if len(string) == 0:
        return []

    if len(string) == 1:
        return [string]

    perms = []

    for i in range(len(string)):
        char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        sub_perms = permutations(remaining_chars)

        for perm in sub_perms:
            perms.append(char + perm)

    return perms