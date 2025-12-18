"""
QUESTION:
Implement a function named `numPermsDISequence(S)` that takes a string `S` of length `n` consisting of characters 'D' and 'I' as input, and returns the number of valid permutations of integers `{0, 1, ..., n}` that satisfy the given conditions modulo `10^9 + 7`. 

The conditions for a valid permutation are as follows: 
- If `S[i] == 'D'`, then `P[i] > P[i+1]`.
- If `S[i] == 'I'`, then `P[i] < P[i+1]`.
 
The length of `S` is in the range `[1, 200]`.
"""

def numPermsDISequence(S):
    MOD = 10**9 + 7
    N = len(S)
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(i+1):
            if S[i-1] == 'I':
                dp[i][j] = sum(dp[i-1][:j]) % MOD
            else:
                dp[i][j] = sum(dp[i-1][j:i]) % MOD
    return sum(dp[N]) % MOD