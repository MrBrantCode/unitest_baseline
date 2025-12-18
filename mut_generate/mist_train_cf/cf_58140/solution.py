"""
QUESTION:
Implement a function `D(N, K)` that calculates the summation of `d(n, k)` for all `1 ≤ n ≤ N` and `1 ≤ k ≤ K`, where `d(n, k)` is the total number of methods to express `n` as a product of `k` ordered integers such that `n = x1 * x2 * ... * xk` and `1 ≤ x1 ≤ x2 ≤ ... ≤ xk`. The result should be returned modulo `1,000,000,007`.
"""

def D(N, K):
    """
    This function calculates the summation of d(n, k) for all 1 ≤ n ≤ N and 1 ≤ k ≤ K,
    where d(n, k) is the total number of methods to express n as a product of k ordered integers
    such that n = x1 * x2 * ... * xk and 1 ≤ x1 ≤ x2 ≤ ... ≤ xk.
    The result is returned modulo 1,000,000,007.

    Args:
        N (int): The upper limit for n.
        K (int): The upper limit for k.

    Returns:
        int: The summation of d(n, k) for all 1 ≤ n ≤ N and 1 ≤ k ≤ K, modulo 1,000,000,007.
    """
    mod = 1000000007
    # initializing the dp table
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    # base case dp[0][0] = 1
    dp[0][0] = 1

    # dynamic programming state transition
    for j in range(1, K+1):
        for i in range(1, N+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            # applying the modulo operation
            dp[i][j] %= mod
            if i < j:
                dp[i][j] -= dp[i-1][j-1]
                # applying the modulo operation
                dp[i][j] %= mod

    return dp[N][K]