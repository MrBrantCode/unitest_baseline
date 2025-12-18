"""
QUESTION:
Write a function `drumMusic(glavList, N, X, G, L)` that takes a list of integers `glavList` and four integers `N`, `X`, `G`, `L` as input, and returns the result of a dynamic programming calculation. The function should use a 3D list `dp` of size `(G+1) x (L+1) x (N+1)` to store intermediate results. The calculation involves iterating over `dp` and updating its values based on certain conditions. The final result is the summation of `dp[G][L][k]` for `k` ranging from `G` to `N`. The calculation should be performed modulo `10**9 + 7`.
"""

def drumMusic(glavList, N, X, G, L):
    mod = 10**9 + 7
    # initialize dp as a 3D list filled with zeroes
    dp = [[[0] * (N + 1) for _ in range(L + 1)] for _ in range(G + 1)]
    dp[0][0][0] = 1
    for i in range(1, G + 1):
        for j in range(1, L + 1):
            for k in range(1, N + 1):
                # play a song from a new genre
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] * (N - k + 1) * glavList[i - 1] % mod
                # play a song from an old genre
                if j >= i * (glavList[i - 1] + 1):
                    dp[i][j][k] += dp[i][i - 1][k] * max(0, j - k * (glavList[i - 1] + 1)) % mod
    # find the summation of dp[G][L][k]
    ans = sum(dp[G][L][k] for k in range(G, N + 1)) % mod
    return ans