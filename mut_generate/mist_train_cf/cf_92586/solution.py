"""
QUESTION:
Create a function called `permute` that generates all permutations of a given input array in lexicographically sorted order. The function should take a list of integers as input and return a list of lists, where each sublist is a permutation of the input array. The function should not use any external libraries or built-in permutation functions.
"""

def permute(nums):
    nums.sort()
    permutations = []
    def backtrack(curr_permutation, remaining_elements):
        if len(remaining_elements) == 0:
            permutations.append(curr_permutation)
            return
        for i in range(len(remaining_elements)):
            next_element = remaining_elements[i]
            remaining = remaining_elements[:i] + remaining_elements[i+1:]
            backtrack(curr_permutation + [next_element], remaining)
    backtrack([], nums)
    return permutations