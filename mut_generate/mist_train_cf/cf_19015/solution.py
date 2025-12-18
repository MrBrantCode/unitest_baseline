"""
QUESTION:
Write a function `max_sum_divisible_by_m` that takes three inputs: an array of positive integers, an integer k, and an integer m. The function should return the maximum sum of k consecutive elements in the array that is divisible by m. The solution should have a time complexity of O(n), where n is the length of the array.
"""

def max_sum_divisible_by_m(array, k, m):
    window_sum = sum(array[:k])  # Initial sum of first window
    max_sum = 0

    if window_sum % m == 0:
        max_sum = window_sum

    for i in range(k, len(array)):
        window_sum += array[i] - array[i - k]
        if window_sum % m == 0:
            max_sum = max(max_sum, window_sum)

    return max_sum