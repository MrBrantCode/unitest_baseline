"""
QUESTION:
Implement a function `backtrack(permutation, unused, n)` that calculates the number of valid permutations of length n with respect to a given set of n distinct elements. The function should use recursion and backtracking to try adding elements to the permutation while satisfying the constraints that each element can only appear once in a permutation. The base case is when the length of the current permutation is equal to n. In each recursive call, iterate over the unused elements and try to add them to the current permutation. The function should return the total count of valid permutations. The function will be called with an empty permutation and the list of all n distinct elements.
"""

def backtrack(permutation, unused, n):
    if len(permutation) == n:
        return 1

    count = 0
    for element in unused:
        if len(permutation) == 0 or element > permutation[-1]:
            new_permutation = permutation + [element]
            new_unused = unused.copy()
            new_unused.remove(element)
            count += backtrack(new_permutation, new_unused, n)

    return count