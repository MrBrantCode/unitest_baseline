"""
QUESTION:
You are given a set of non-negative integers and a value `sum`, determine if there is a subset of the given set with sum equal to given `sum`. 

Write a function `isSubsetSum(set, n, sum)` where `set` is the given set of integers, `n` is the number of elements in the set, and `sum` is the target sum. 

Constraints:
`1 <= n <= 30`
`0 <= set[i] <= 200`
All elements of `set` are distinct.
`1 <= sum <= 500`
"""

def isSubsetSum(set, n, sum):
    """
    Determine if there is a subset of the given set with sum equal to given sum.

    Args:
        set (list): A set of non-negative integers.
        n (int): The number of elements in the set.
        sum (int): The target sum.

    Returns:
        bool: True if a subset with the target sum exists, False otherwise.
    """
    subset = [[False for _ in range(sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        subset[i][0] = True

    for i in range(1, sum + 1):
        subset[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i - 1][j-set[i-1]])

    return subset[n][sum]