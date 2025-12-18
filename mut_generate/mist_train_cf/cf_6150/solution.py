"""
QUESTION:
Write a function named `generate_all_permutations` that generates all possible permutations of a given list of numbers, including duplicates, in lexicographically increasing order. The function should take a list of numbers as input, handle lists with up to 10^6 elements efficiently, and return the list of permutations.
"""

def generate_all_permutations(nums):
    permutations = []

    def generate_permutations(current_permutation, remaining_elements):
        if len(remaining_elements) == 0:
            permutations.append(current_permutation)
        else:
            for i in range(len(remaining_elements)):
                new_permutation = current_permutation + [remaining_elements[i]]
                new_remaining_elements = remaining_elements[:i] + remaining_elements[i+1:]
                generate_permutations(new_permutation, new_remaining_elements)

    generate_permutations([], sorted(nums))
    return permutations