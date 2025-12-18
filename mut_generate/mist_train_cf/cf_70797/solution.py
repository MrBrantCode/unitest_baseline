"""
QUESTION:
Write a function `Q(n)` that calculates the number of permissible paths from point `(n, n)` to `(0, 0)` using only unit steps south or west, where a path is considered permissible if none of its intermediate points are forbidden. A lattice point `(x, y)` is considered forbidden if `x`, `y`, and `x-y` are all positive perfect cubes. The function should return the result modulo `1,000,000,007`.
"""

def Q(n):
    MAXN = n + 1

    cube = [i**3 for i in range(47)] 
    cube_set = set(cube)

    dp = [[0]*MAXN for _ in range(MAXN)]
    dp[MAXN-1][MAXN-1] = 1

    forbidden = [[(x**3, y**3) in cube_set for y in range(MAXN)] for x in range(MAXN)]

    MOD = 1_000_000_007
    for x in range(MAXN-2, -1, -1):
        for y in range(MAXN-2, -1, -1):
            if forbidden[x][y] or forbidden[y][x]:
                dp[x][y] = 0
            else:
                dp[x][y] = (dp[x+1][y] + dp[x][y+1]) % MOD

    return dp[0][0]