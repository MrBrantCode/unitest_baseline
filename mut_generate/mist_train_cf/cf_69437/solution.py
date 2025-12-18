"""
QUESTION:
Write a function `subarray_sum` that takes a list of integers `lst` and an integer `k` as input, and returns all subarrays of consecutive integers in `lst` whose sum equals `k`.
"""

def subarray_sum(lst, k):
    results = []
    for i in range(len(lst)):
        sum = 0
        for j in range(i, len(lst)):
            sum += lst[j]
            if sum == k:
                results.append(lst[i:j+1])
    return results