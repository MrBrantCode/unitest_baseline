"""
QUESTION:
Write a function named `generate_random_permutation` that takes an array `arr` as input and returns a random permutation of `arr` such that no two consecutive elements are equal. The function should have a time complexity of O(n) and should not use any additional libraries. The input array can contain duplicate elements and will have at least two distinct elements.
"""

import random

def generate_random_permutation(arr):
    n = len(arr)
    result = [0] * n
    count = [0] * (max(arr) + 1)

    for i in arr:
        count[i] += 1

    for i in range(n):
        max_count = 0
        max_index = -1

        for j in range(len(count)):
            if count[j] > max_count and (i == 0 or j != result[i - 1]):
                max_count = count[j]
                max_index = j

        result[i] = max_index
        count[max_index] -= 1

    return result