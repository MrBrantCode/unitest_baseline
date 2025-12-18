"""
QUESTION:
Implement a function `numberOfPatterns` that takes two integers `m` and `n` as input and returns the total number of unlock patterns that consist of `m` to `n` points, following these rules:

- The unlock pattern can start from any number.
- A valid unlock pattern can contain at most one cross, where a cross is a line that connects two points that have a number in between them that is also in the pattern.
- Two points cannot be connected if the number in between them is already in the pattern.

The `numberOfPatterns` function should call a helper function `dfs` that performs a depth-first search to explore all possible patterns. The `dfs` function takes a list `visit` to keep track of visited points, a 2D list `skip` to store the numbers that are skipped when connecting two points, the current point `cur`, and the remaining number of points `remain` to visit.

The `skip` list is initialized with the following rules: 
- `skip[1][3] = skip[3][1] = 2`
- `skip[1][7] = skip[7][1] = 4`
- `skip[1][9] = skip[9][1] = 5`
- `skip[2][8] = skip[8][2] = 5`
- `skip[3][7] = skip[7][3] = 5`
- `skip[3][9] = skip[9][3] = 6`
- `skip[4][6] = skip[6][4] = 5`
- `skip[7][9] = skip[9][7] = 8`
"""

def numberOfPatterns(m, n):
    skip = [[0]*10 for _ in range(10)]
    skip[1][7] = skip[7][1] = 4
    skip[1][3] = skip[3][1] = 2
    skip[3][9] = skip[9][3] = 6
    skip[7][9] = skip[9][7] = 8
    skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
    visit = [False]*10
    ans = 0
    for l in range(m, n+1):
        ans += dfs(visit, skip, 1, l-1)*4  # 1, 3, 7, 9 are symmetric
        ans += dfs(visit, skip, 2, l-1)*4  # 2, 4, 6, 8 are symmetric
        ans += dfs(visit, skip, 5, l-1)    # 5
    return ans

def dfs(visit, skip, cur, remain):
    if remain < 0:
        return 0
    if remain == 0:
        return 1
    visit[cur] = True
    ans = 0
    for i in range(1,10):
        if not visit[i] and (skip[cur][i] == 0 or (visit[skip[cur][i]])):
            ans += dfs(visit, skip, i, remain-1)
    visit[cur] = False
    return ans