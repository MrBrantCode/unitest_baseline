"""
QUESTION:
Given an array of positive integers, write a function `max_sum_subarray_with_duplicates` that finds the maximum sum of a subarray where all its elements appear in the array at least twice. The subarray must have a length of at least two. The function should return the maximum possible sum of such a subarray. The input array contains only positive integers.
"""

def max_sum_subarray_with_duplicates(arr):
    n = len(arr)
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    dp = [[-float('inf')] * n for _ in range(n)]
    max_sum = -float('inf')

    for i in range(n):
        dp[i][i] = freq[arr[i]] * arr[i] if freq[arr[i]] > 1 else 0
        max_sum = max(max_sum, dp[i][i])

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            freq_count = {}
            for k in range(i, j + 1):
                freq_count[arr[k]] = freq_count.get(arr[k], 0) + 1
            
            valid = True
            for count in freq_count.values():
                if count < 2:
                    valid = False
                    break
            
            if valid:
                dp[i][j] = sum(arr[i:j + 1])
                max_sum = max(max_sum, dp[i][j])

    return max_sum if max_sum > -float('inf') else 0