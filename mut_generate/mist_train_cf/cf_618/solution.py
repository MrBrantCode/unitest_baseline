"""
QUESTION:
Write a function `generate_permutations(string)` to generate a list of all possible permutations of a given string. The generated permutations should not contain any repeating characters and should be sorted in lexicographic order. The length of the given string will not exceed 20 characters. The function should use only recursion and not use any built-in functions or libraries for generating permutations.
"""

def generate_permutations(string):
    if len(string) <= 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        char = string[i]
        remaining_string = string[:i] + string[i+1:]
        sub_permutations = generate_permutations(remaining_string)

        for sub_permutation in sub_permutations:
            new_permutation = char + sub_permutation
            if new_permutation not in permutations:
                permutations.append(new_permutation)

    return sorted(permutations)