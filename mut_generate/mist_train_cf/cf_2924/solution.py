"""
QUESTION:
Write a function `find_subarray(arr, k, p)` that finds the subarray with the largest sum in an integer array `arr` of length `n`, where the subarray must consist of consecutive elements, have a length greater than or equal to `k`, and its sum must be divisible by an integer `p`. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_subarray(arr, k, p):
    n = len(arr)
    max_sum = float('-inf')
    curr_sum = 0
    start = end = 0

    for i in range(n):
        curr_sum += arr[i]

        if curr_sum < 0:
            curr_sum = 0
            start = i + 1

        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i

        if (end - start + 1) >= k and max_sum % p == 0:
            return arr[start:end+1]

    return None