"""
QUESTION:
Write a function `generate_permutations` that generates all permutations of a given list of letters without using any built-in library functions or external modules. The function should take a list of letters as input and return a list of lists, where each sublist is a permutation of the input list.
"""

def generate_permutations(letters):
    if len(letters) == 0:
        return []

    if len(letters) == 1:
        return [letters]

    permutations = []
    for i in range(len(letters)):
        current_letter = letters[i]
        remaining_letters = letters[:i] + letters[i+1:]

        for perm in generate_permutations(remaining_letters):
            permutations.append([current_letter] + perm)

    return permutations