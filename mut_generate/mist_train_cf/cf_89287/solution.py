"""
QUESTION:
Generate all possible permutations of a given list of numbers, including duplicates. The function should be named "generate_all_permutations" and it should take a list of numbers as input. The output should be a list of all permutations in lexicographically increasing order. The function should be able to handle large inputs efficiently and have a time complexity better than O(n!) if possible, where n is the length of the input list.
"""

def generate_all_permutations(nums):
    permutations = set()

    def backtrack(current_permutation, remaining_elements):
        if len(remaining_elements) == 0:
            permutations.add(tuple(current_permutation))
        else:
            for i in range(len(remaining_elements)):
                new_permutation = current_permutation + [remaining_elements[i]]
                new_remaining_elements = remaining_elements[:i] + remaining_elements[i+1:]
                backtrack(new_permutation, new_remaining_elements)

    backtrack([], sorted(nums))
    return [list(p) for p in sorted(permutations)]