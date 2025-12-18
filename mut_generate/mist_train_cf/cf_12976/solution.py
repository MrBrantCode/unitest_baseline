"""
QUESTION:
Write a function named `permute` that takes an array of integers as input and returns all permutations of the input array in lexicographically sorted order. The function should be able to handle arrays of any length and should not take any additional arguments. The input array is not guaranteed to be sorted.
"""

def permute(arr):
    arr.sort()
    permutations = []
    
    def backtrack(curr_permutation, remaining_elements):
        if len(remaining_elements) == 0:
            permutations.append(curr_permutation)
            return
        
        for i in range(len(remaining_elements)):
            next_element = remaining_elements[i]
            remaining = remaining_elements[:i] + remaining_elements[i+1:]
            backtrack(curr_permutation + [next_element], remaining)
    
    backtrack([], arr)
    return permutations