"""
QUESTION:
Generate all possible permutations of the string "ABCXYZ" without repetition.
"""

def generate_permutations(string):
    if len(string) == 1:
        return [string]
    permutations = []
    for i, char in enumerate(string):
        remaining_string = string[:i] + string[i+1:]
        for perm in generate_permutations(remaining_string):
            permutations.append(char + perm)
    return permutations