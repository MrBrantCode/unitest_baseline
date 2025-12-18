"""
QUESTION:
Implement a function `recursiveFun(n, m)` that takes two integers `n` and `m` and returns the number of recursive calls made. The function should handle large values of `n` and `m` efficiently. To achieve this, implement memoization or another optimization strategy to minimize redundant calculations and reduce time complexity. The function should have a base case for when `n` or `m` is less than or equal to 0.
"""

def recursiveFun(n, m, memo):
    # if already solved, return the solution from memo table
    if memo[n][m] != -1: 
        return memo[n][m]

    # base cases
    elif n <= 0 or m <= 0: 
        memo[n][m] = 0
        return 0

    else:
        # computing necessary values
        for i in range(n):
            for j in range(m):
                recursiveFun(i, j, memo)

        # storing calculated value in memo table
        memo[n][m] = 1

    return memo[n][m]