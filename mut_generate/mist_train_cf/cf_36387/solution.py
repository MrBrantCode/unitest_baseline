"""
QUESTION:
Write a function `partitionProblem(num)` that takes a list of positive integers `num` and returns two subsets if the list can be partitioned into two subsets with equal sums, or "Vector can not be partitioned" otherwise. The function should use dynamic programming and return the two subsets as lists of integers if a valid partition exists.
"""

def partitionProblem(num):
    total_sum = sum(num)
    if total_sum % 2 != 0:
        return "\nVector can not be partitioned"

    target_sum = total_sum // 2
    size = len(num)
    dp = [[False for _ in range(target_sum + 1)] for _ in range(size + 1)]

    for i in range(size + 1):
        dp[i][0] = True

    for i in range(1, size + 1):
        for j in range(1, target_sum + 1):
            if j < num[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num[i - 1]]

    if not dp[size][target_sum]:
        return "\nVector can not be partitioned"

    subset1 = []
    subset2 = []
    i, j = size, target_sum
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            i -= 1
        else:
            subset1.append(num[i - 1])
            j -= num[i - 1]
            i -= 1

    subset2 = [x for x in num if x not in subset1]
    return subset1, subset2