"""
QUESTION:
Write a function called `generate_permutations` that generates all distinct permutations of a given string. The function should not use any built-in functions or libraries to generate permutations and should have a time complexity of O(n!). The function should handle strings containing duplicate characters and not generate duplicate permutations.
"""

def generate_permutations(string):
    n = len(string)
    permutations = []
    stack = []
    stack.append(("", set()))

    while stack:
        permutation, visited_indices = stack.pop()

        if len(permutation) == n:
            permutations.append(permutation)
            continue

        for i in range(n):
            if i not in visited_indices:
                new_permutation = permutation + string[i]
                new_visited_indices = visited_indices.copy()
                new_visited_indices.add(i)
                stack.append((new_permutation, new_visited_indices))

    return permutations