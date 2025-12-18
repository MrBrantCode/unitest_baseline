"""
QUESTION:
Write a function named `max_sum_divisible` that takes an array of positive integers, an integer `k`, and an integer `m` as input. The function should return the smallest maximum sum of `k` consecutive elements in the array that is divisible by `m`. If no such sum exists, the function should return `None`. The time complexity of the solution should be O(n), where n is the length of the array.
"""

def max_sum_divisible(arr, k, m):
    if k > len(arr):
        return None

    max_sum = 0
    possible_sums = []
    for i in range(len(arr) - k + 1):
        curr_sum = sum(arr[i:i+k])
        if curr_sum % m == 0:
            possible_sums.append(curr_sum)
    if len(possible_sums) == 0:
        return None
    return min(possible_sums)