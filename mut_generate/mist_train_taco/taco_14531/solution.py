"""
QUESTION:
Example

Input

2 2
..
..


Output

Second
"""

def determine_winner(H, W, grid):
    def dfs(px, py, qx, qy):
        key = (px, py, qx, qy)
        if key in memo:
            return memo[key]
        res = set()
        for y in range(py, qy):
            for x in range(px, qx):
                if S[y][x]:
                    continue
                r1 = dfs(px, py, x, y)
                r2 = dfs(x + 1, py, qx, y)
                r3 = dfs(px, y + 1, x, qy)
                r4 = dfs(x + 1, y + 1, qx, qy)
                res.add(r1 ^ r2 ^ r3 ^ r4)
        k = 0
        while k in res:
            k += 1
        memo[key] = k
        return k

    f = '.X'.index
    S = [list(map(f, row)) for row in grid]
    memo = {}

    if dfs(0, 0, W, H):
        return 'First'
    else:
        return 'Second'