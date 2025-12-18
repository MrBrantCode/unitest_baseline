"""
QUESTION:
Write a function `permutations(arr)` that generates all permutations of the input array `arr`. The function should return a list of lists, where each sublist is a unique permutation of the input array. The input array will contain distinct elements.
"""

def permute(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]

    smaller_permutations = permute(arr[1:])
    current_element = arr[0]
    permutations_for_current_element = []

    for per in smaller_permutations:
        for i in range(len(per)+1):
            new_permutation = per[:]
            new_permutation.insert(i, current_element)
            permutations_for_current_element.append(new_permutation)

    return permutations_for_current_element