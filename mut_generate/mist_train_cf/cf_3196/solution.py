"""
QUESTION:
Implement a function named `get_permutations` that takes a string as input and returns a list of all possible permutations of that string without using any built-in functions, libraries, recursion, or backtracking techniques. The time complexity should be less than O(n!) and the space complexity should be less than O(n!), where n is the length of the input string.
"""

def get_permutations(string):
    permutations = []
    if len(string) == 0:
        return permutations

    stack = [(string, '')]
    while stack:
        current_string, current_permutation = stack.pop()
        if len(current_permutation) == len(string):
            permutations.append(current_permutation)
        for i in range(len(current_string)):
            new_string = current_string[:i] + current_string[i+1:]
            new_permutation = current_permutation + current_string[i]
            stack.append((new_string, new_permutation))

    return permutations