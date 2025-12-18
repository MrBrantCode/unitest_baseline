"""
QUESTION:
Define a function `B(M)` that returns the number of quadruples `(x, y, z, w)` of positive integers, where `0 < x < y`, `0 < z < w`, `w <= M`, the sum of the proper divisors of `x` and `y` equals `z`, and the sum of the proper divisors of `z` and `w` equals `y`. Implement the function `B(M)` with the constraint that `M` is a positive integer and `M = 10^18`.
"""

def B(M):
    # Initialize variables
    MAX_LOG2 = 61
    MAX_J = int(M**0.5)
    MAX_I = int(M)

    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(MAX_LOG2 + 1)]
    S = [[0 for _ in range(MAX_J + 1)] for _ in range(MAX_I + 1)]

    # Initialize base cases
    for i in range(MAX_LOG2 + 1):
        dp[i][0][0] = 1

    # Calculate S for each j
    for j in range(1, MAX_J + 1):
        S[j][j] = 1

    # Calculate S for each i
    for i in range(2, MAX_I + 1):
        for j in range(1, min(i // 2 + 1, MAX_J + 1)):
            S[i][j] = S[i - 1][j] + S[j][i // 64 - j]

    # Calculate the result
    result = 0
    for i in range(MAX_I + 1):
        for j in range(1, min(i // 2 + 1, MAX_J + 1)):
            result += S[i][j]

    return result