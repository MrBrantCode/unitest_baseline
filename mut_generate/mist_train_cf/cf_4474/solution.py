"""
QUESTION:
Write a function `generate_permutations(arr, n)` that generates n! permutations of a given array `arr` of length `n`. The function should not use the itertools library or any built-in functions that directly solve this problem and should have a time complexity of O(n!).
"""

def generate_permutations(arr, n):
    result = []  # to store the permutations
    generate_permutations_helper(arr, 0, n, result)
    return result


def generate_permutations_helper(arr, start, n, result):
    if start == n - 1:
        result.append(arr.copy())  # add the current permutation to the result
    else:
        for i in range(start, n):
            arr[start], arr[i] = arr[i], arr[start]  # swap elements
            generate_permutations_helper(arr, start + 1, n, result)  # recursively generate permutations
            arr[start], arr[i] = arr[i], arr[start]  # revert the swap