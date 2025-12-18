"""
QUESTION:
Write a function `dp_algo` that calculates the maximum sum of non-adjacent elements in a list from index 0 to n. The function should take two parameters: `n`, the index up to which the sum is calculated, and `arr`, the list of elements. The function should return the maximum sum of non-adjacent elements.

Restrictions: The function should use dynamic programming principles to avoid recalculating the sum for each position multiple times and improve efficiency.
"""

def dp_algo(n, arr):
    if n < 1:
        return 0
    else:
        sums = [0] * n
        sums[0] = arr[0]
        if n > 1:
            sums[1] = max(arr[0], arr[1])
        for i in range(2, n):
            sums[i] = max(sums[i-1], sums[i-2] + arr[i])
        return sums[-1]