"""
QUESTION:
Design an algorithm for a function named `find_longest_increasing_subsequence` that finds the longest increasing subsequence in a given array of positive integers. The subsequence should be strictly increasing, meaning each element in the subsequence should be greater than the previous element. The function should return the longest increasing subsequence itself, not just its length.
"""

def find_longest_increasing_subsequence(arr):
    n = len(arr)

    # Handle edge cases
    if n == 0:
        return []
    elif n == 1:
        return arr

    lengths = [1] * n
    prev_indices = [-1] * n

    max_length = 1
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j

                if lengths[i] > max_length:
                    max_length = lengths[i]
                    max_index = i

    # Reconstruct the subsequence
    subsequence = []
    index = max_index
    while index >= 0:
        subsequence.append(arr[index])
        index = prev_indices[index]

    return subsequence[::-1]