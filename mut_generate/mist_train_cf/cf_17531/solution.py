"""
QUESTION:
Write a function `permutations(arr)` to generate all permutations of the given list `arr` without using any built-in library functions or external modules. The function should handle lists with duplicate elements and return the permutations in lexicographically sorted order.
"""

def permutations(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]

    result = []

    used = set()  # Track used elements

    for i in range(len(arr)):
        if arr[i] in used:  # Skip duplicate elements
            continue

        used.add(arr[i])

        m = arr[i]

        rem_list = arr[:i] + arr[i+1:]

        for p in permutations(rem_list):
            result.append([m] + p)

    return sorted(result)