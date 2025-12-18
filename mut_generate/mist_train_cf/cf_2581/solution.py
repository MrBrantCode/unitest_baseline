"""
QUESTION:
Write a function `find_subarray` that takes an array of integers, an integer `k`, and a positive integer `m` as input. The function should return the subarray with the maximum sum less than `k`, where the subarray has a length greater than or equal to `m` and contains at least one negative number and one positive number. If multiple subarrays have the same maximum sum, return the subarray with the smallest length. If no such subarray exists, return an empty array. The function should have a time complexity of O(n^2), where n is the length of the array, and a space complexity of O(1).
"""

def find_subarray(arr, k, m):
    n = len(arr)
    max_sum = float('-inf')
    subarray = []
    found_subarray = False

    for i in range(n - m + 1):
        for j in range(i + m - 1, n):
            current_sum = sum(arr[i:j + 1])
            contains_negative = any(num < 0 for num in arr[i:j + 1])
            contains_positive = any(num > 0 for num in arr[i:j + 1])

            if current_sum < k and current_sum > max_sum and contains_negative and contains_positive:
                max_sum = current_sum
                subarray = arr[i:j + 1]
                found_subarray = True

    if not found_subarray:
        return []

    min_length = len(subarray)
    result = subarray

    for i in range(n - m + 1):
        for j in range(i + m - 1, n):
            current_sum = sum(arr[i:j + 1])
            contains_negative = any(num < 0 for num in arr[i:j + 1])
            contains_positive = any(num > 0 for num in arr[i:j + 1])

            if current_sum < k and current_sum == max_sum and contains_negative and contains_positive:
                if len(arr[i:j + 1]) < min_length:
                    min_length = len(arr[i:j + 1])
                    result = arr[i:j + 1]

    return result