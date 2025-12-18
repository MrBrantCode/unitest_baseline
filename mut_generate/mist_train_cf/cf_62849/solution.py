"""
QUESTION:
Write a function `catalan_numbers(n)` that generates the nth Catalan number efficiently and accurately, handling large integer arithmetic. The function should use dynamic programming to avoid redundant computations. The solution should also be able to handle large values of n, such as n = 50, without significant performance degradation. The output should be an integer or a decimal number with high precision.
"""

from decimal import Decimal, getcontext

getcontext().prec = 100

def catalan(n):
    if n <= 1:
        return 1

    dp = [0 for _ in range(n+1)]
    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        dp[i] = Decimal(0)
        for j in range(i):
            dp[i] += Decimal(dp[j]) * Decimal(dp[i-j-1])

    return dp[n]