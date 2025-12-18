"""
QUESTION:
Write a function named `generate_permutations` that takes a string of up to 10 characters as input, and returns all permutations of the string in lexicographic order without using any built-in libraries or functions for generating permutations. The function should efficiently handle cases where the input string may contain duplicate characters.
"""

def generate_permutations(string):
    permutations = set()
    generate_permutations_helper(list(string), 0, len(string) - 1, permutations)
    return sorted(list(permutations))

def generate_permutations_helper(string_list, start, end, permutations):
    if start == end:
        permutation = ''.join(string_list)
        permutations.add(permutation)
    else:
        for i in range(start, end + 1):
            if not should_swap(string_list, start, i):
                continue
            string_list[start], string_list[i] = string_list[i], string_list[start]
            generate_permutations_helper(string_list, start + 1, end, permutations)
            string_list[start], string_list[i] = string_list[i], string_list[start]

def should_swap(string_list, start, curr):
    for i in range(start, curr):
        if string_list[i] == string_list[curr]:
            return False
    return True