"""
QUESTION:
Write a function `longest_common_substring_product` that takes two lists of integers as input and returns the product of their longest common strictly increasing subsequence. The function should only consider subsequences of length 3 or more. If multiple subsequences have the same maximum length, return the product of the one that starts at the earliest index in the first list. If no common subsequences exist, return 0.
"""

def longest_common_substring_product(list1, list2):
    n = len(list1)
    m = len(list2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    longest_len = 0
    longest_end = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if list1[i - 1] == list2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] >= 3 and dp[i][j] > longest_len:
                    longest_len = dp[i][j]
                    longest_end = i

    if longest_len == 0:
        return 0

    longest_start = longest_end - longest_len
    longest_substring = list1[longest_start:longest_end]
    product = 1
    for num in longest_substring:
        product *= num

    return product