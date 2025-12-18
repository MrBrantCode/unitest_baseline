"""
QUESTION:
Write a function named `max_sum_divisible` that takes in a list of positive integers `lst` and an integer `divisor`. The function should return the maximum possible sum of a subset of the integers in `lst` that meets the following conditions: the sum of the integers in the subset is divisible by `divisor`, and no two consecutive integers from `lst` are in the subset. The time complexity of the function should be O(n * k), where n is the length of `lst` and k is the maximum value in `lst`.
"""

def max_sum_divisible(lst, divisor):
    n = len(lst)
    dp = [[0] * (divisor + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(divisor + 1):
            if j < lst[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][(j - lst[i - 1]) % divisor] + lst[i - 1])

    return dp[n][0]