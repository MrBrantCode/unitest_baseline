"""
QUESTION:
Write a function named `generate_permutations_recursive` that generates all permutations of a given string in lexicographic order without using any built-in libraries or functions for generating permutations. The function should be able to handle strings of length up to 15 characters and efficiently handle cases where the input string may contain duplicate characters. The function should optimize memory usage and minimize the use of additional data structures. The time complexity of the function should be O(n!) where n is the length of the input string. The function should take four parameters: a string, the current permutation, a list of boolean values indicating whether a character has been used, and a list to store the generated permutations.
"""

def generate_permutations_recursive(string, current_permutation, used, permutations):
    # Base case: if the current permutation is complete
    if len(current_permutation) == len(string):
        permutations.append(current_permutation)
        return

    # Recursive case: generate permutations by trying all possible characters
    for i in range(len(string)):
        if used[i]:
            continue
        if i > 0 and string[i] == string[i - 1] and not used[i - 1]:
            continue
        used[i] = True
        generate_permutations_recursive(string, current_permutation + string[i], used, permutations)
        used[i] = False