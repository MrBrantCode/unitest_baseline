"""
QUESTION:
Given two integers m and n (1 <= m, n <= 9), determine the number of unique and valid unlock patterns of the Android grid lock screen that comprise at least m keys and at most n keys. A valid unlock pattern is one where each dot in the sequence is unique and if a line segment that links two successive dots in the sequence traverses any other dot, that other dot must have been included in the sequence earlier. Write a function named numberOfPatterns that returns the count of such patterns.
"""

def numberOfPatterns(m: int, n: int) -> int:
    skip = [[0]*10 for _ in range(10)]
    skip[1][3] = skip[3][1] = 2
    skip[1][7] = skip[7][1] = 4
    skip[3][9] = skip[9][3] = 6
    skip[7][9] = skip[9][7] = 8
    skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
    visit = [0]*10
    ans = 0
    def dfs(cur, remain):
        if remain < 0:
            return 0
        if remain == 0:
            return 1
        visit[cur] = True
        res = 0
        for i in range(1,10):
            if not visit[i] and (skip[cur][i] == 0 or visit[skip[cur][i]]):
                res += dfs(i, remain-1)
        visit[cur] = False
        return res
    for i in range(m,n+1):
        ans += dfs(1, i-1)*4  # 1, 3, 7, 9 are symmetric
        ans += dfs(2, i-1)*4  # 2, 4, 6, 8 are symmetric
        ans += dfs(5, i-1)    # 5
    return ans