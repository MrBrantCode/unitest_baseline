"""
QUESTION:
Write a function `max_sum_of_lengths` that takes an integer `n`, a list of strings `data`, and an integer `k` as input, where `n` is the number of elements in the array, `1 <= n <= 10^5`, `data` is the array of strings with `1 <= len(data) <= n` and `1 <= len(data[i]) <= 10`, and `k` is the number of non-overlapping subarrays to consider with `1 <= k <= n`. The function should return the maximum sum of the lengths of `k` non-overlapping subarrays, where each subarray contains only distinct elements. If there are multiple possible combinations that result in the same maximum sum, the function should return the lexicographically smallest combination.
"""

def max_sum_of_lengths(n, data, k):
    max_sum = 0
    for i in range(len(data)):
        subarray_set = set()
        current_sum = 0
        for j in range(i, len(data)):
            if data[j] not in subarray_set:
                subarray_set.add(data[j])
                current_sum += len(data[j])
                if len(subarray_set) == k:
                    if current_sum > max_sum:
                        max_sum = current_sum
            else:
                break
    return max_sum