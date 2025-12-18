"""
QUESTION:
Implement a function named `count_valid_permutations(n)` that takes an integer `n` as input, representing the number of distinct elements. The function should return the number of valid permutations of length `n`, where each element can appear exactly once, and each element in a permutation must be greater than its preceding element.
"""

def count_valid_permutations(n):
    elements = list(range(1, n+1))
    permutation = []
    unused_elements = elements.copy()
    counter = 0

    def backtrack(permutation, unused_elements):
        if len(permutation) == n:
            nonlocal counter
            counter += 1
            return
        
        for element in unused_elements:
            if len(permutation) == 0 or element > permutation[-1]:
                new_permutation = permutation.copy()
                new_permutation.append(element)
                new_unused_elements = unused_elements.copy()
                new_unused_elements.remove(element)
                backtrack(new_permutation, new_unused_elements)
    
    backtrack(permutation, unused_elements)
    return counter