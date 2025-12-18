"""
QUESTION:
Write a function named `generate_random_permutation` that generates a random permutation of a given array, ensuring that no two consecutive elements in the permutation are equal. The function should have a time complexity of O(n) and should not use any additional libraries. The input array can be of any size but will not exceed 10^5 elements and will always have at least two distinct elements.
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