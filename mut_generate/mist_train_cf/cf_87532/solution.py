"""
QUESTION:
Write a function called `find_subarray` that takes in three parameters: `arr` (an array of integers), `k` (an integer), and `m` (a positive integer). The function should return the subarray with the maximum sum less than `k`, with a length of at least `m`, and containing at least one negative and one positive number. If multiple subarrays have the same maximum sum, return the one with the smallest length. If no such subarray exists, return an empty array. The function should have a time complexity of O(n^2), where n is the length of `arr`, and a space complexity of O(1).
"""

def find_subarray(arr, k, m):
    n = len(arr)
    max_sum = float('-inf')
    subarray = []
    found_subarray = False
    has_negative_and_positive = False

    for i in range(n - m + 1):
        for j in range(i, n):
            current_sum = sum(arr[i:j + 1])
            has_negative_and_positive = any(x < 0 for x in arr[i:j + 1]) and any(x > 0 for x in arr[i:j + 1])
            if (j - i + 1) >= m and current_sum < k and current_sum > max_sum and has_negative_and_positive:
                max_sum = current_sum
                subarray = arr[i:j + 1]
                found_subarray = True

    if not found_subarray:
        return []

    return subarray