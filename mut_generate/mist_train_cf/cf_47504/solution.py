"""
QUESTION:
Function `numMusicPlaylists(N, L, K, G)` calculates the number of possible playlists of `L` songs from `N` songs in `G` genres, where every song is played at least once, a song can only be played again only if `K` other songs have been played, and no two songs from the same genre can be played consecutively. Return the number of possible playlists modulo `10^9 + 7`. The given constraints are `0 <= K < N <= L <= 100` and `1 <= G <= N`.
"""

mod = 10**9 + 7

def numMusicPlaylists(N, L, K, G):
    # Initialize dp as a 3D list filled with zeroes
    dp = [[[0] * (N + 1) for _ in range(L + 1)] for _ in range(G + 1)]
    dp[0][0][0] = 1
    for i in range(1, G + 1):
        for j in range(1, L + 1):
            for k in range(1, N + 1):
                # Play a song from a new genre
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] * (N - k + 1) * N % mod
                # Play a song from an old genre
                if j >= i * (K + 1):
                    dp[i][j][k] += dp[i][j - 1][k] * max(0, k * (K + 1) - j) % mod
    # Find the summation of dp[G][L][k]
    ans = sum(dp[G][L][k] for k in range(G, N + 1)) % mod
    return ans