"""
QUESTION:
Create a function `get_all_permutations` that returns all unique permutations of the input string. The function should take one parameter, `string`, and return a list of all possible permutations. The input string can be any length, but the function should be able to handle strings of at least length 1.
"""

def get_all_permutations(string):
    if len(string) == 1:
        return [string]

    permutations = []
    for index, char in enumerate(string):
        slice_string = string[:index] + string[index+1:]
        for permutation in get_all_permutations(slice_string):
            permutations.append(char + permutation)

    return permutations