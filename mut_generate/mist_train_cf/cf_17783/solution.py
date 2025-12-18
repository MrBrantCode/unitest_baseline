"""
QUESTION:
Write a function named `find_largest_sum_subarray` that takes an integer array `arr` and an integer `k` as input, and returns the subarray with the largest sum that has a length of at least `k`. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.
"""

def find_largest_sum_subarray(arr, k):
    n = len(arr)
    if k > n:
        return None

    max_sum = float('-inf')
    current_sum = 0
    start_index = 0

    for i in range(n):
        current_sum += arr[i]

        if i >= k - 1:
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i - k + 1

            current_sum -= arr[i - k + 1]

    return arr[start_index:start_index + k]