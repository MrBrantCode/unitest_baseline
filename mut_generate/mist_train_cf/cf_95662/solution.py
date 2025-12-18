"""
QUESTION:
Write a function named `generate_permutations` that generates all permutations of a given string in lexicographic order, without using any built-in libraries or functions for generating permutations. The function should be able to handle strings of length up to 15 characters, efficiently handle cases where the input string may contain duplicate characters, and optimize memory usage and minimize the use of additional data structures. The time complexity of the function should be O(n!) where n is the length of the input string.
"""

def generate_permutations(string):
    sorted_string = ''.join(sorted(string))
    permutations = []
    used = [False] * len(string)
    def generate_permutations_recursive(current_permutation):
        if len(current_permutation) == len(string):
            permutations.append(current_permutation)
            return
        for i in range(len(string)):
            if used[i]:
                continue
            if i > 0 and string[i] == string[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            generate_permutations_recursive(current_permutation + string[i])
            used[i] = False
    generate_permutations_recursive("")
    return permutations