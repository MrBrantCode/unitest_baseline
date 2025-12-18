"""
QUESTION:
Write a function `S(n)` that calculates the maximum number of stations that can be traversed on a route from `(0, 0)` to `(n, n)` such that the `x` and `y` coordinates never decrease during the journey, where stations are located at coordinates `(x, y) = (2^i mod n, 3^i mod n)` for `0 <= i <= 2n`. Stations sharing the same coordinates are regarded as a single station. The function should take a positive integer `n` as input and return the maximum number of stations that can be traversed.

The function `S(n)` will be used to calculate the sum of `S(k^5)` for `1 <= k <= 30`.
"""

def S(n):
    stations = sorted((pow(2, i, n), pow(3, i, n)) for i in range(2 * n + 1))
    dp = [0] * len(stations)
    for i in range(len(stations)):
        dp[i] = max((dp[j] + 1 for j in range(i) if stations[j][0] <= stations[i][0] and stations[j][1] <= stations[i][1]), default=1)
    return max(dp)