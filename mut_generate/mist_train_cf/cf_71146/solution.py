"""
QUESTION:
Write a function `longest_common_subarray(arr1, arr2)` that takes two lists of integers as input and returns the longest continuous subarray common to both lists and its length. The function should return one of the longest common subarrays if there are multiple. The input lists are not guaranteed to be of the same length.
"""

def longest_common_subarray(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    dp = [[0] * (arr2_len+1) for _ in range(arr1_len+1)]

    max_len = max_index = 0

    for i in range(1, arr1_len+1):
        for j in range(1, arr2_len+1):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    max_index = i - 1

    return arr1[max_index - max_len + 1 : max_index + 1], max_len