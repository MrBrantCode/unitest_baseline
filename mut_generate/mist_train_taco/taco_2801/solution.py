"""
QUESTION:
Sunuke-kun's dictionary contains the words s1, ..., sn, which consist of n lowercase letters. This satisfies s1 <... <sn when compared in lexicographical order. Unfortunately, some characters are faint and unreadable. Unreadable characters are represented by?. Find out how many ways to restore the dictionary by replacing? With lowercase letters, even with mod 1,000,000,007.

Constraints

* 1 ≤ n ≤ 50
* 1 ≤ | si | ≤ 20
* The characters that appear in si are lowercase letters or?

Input


n
s1
.. ..
sn


Output

Print the answer on one line.

Examples

Input

2
?sum??mer
c??a??mp


Output

703286064


Input

3
snuje
????e
snule


Output

1
"""

def count_restoration_ways(n, words):
    MOD = 10**9 + 7
    M = 20
    L = 26
    ca = ord('a')
    cq = ord('?')
    
    # Initialize the 2D list S with ord('a') - 1
    S = [[ca - 1] * M for _ in range(n)]
    
    # Fill S with the ord values of the characters in the words
    for i in range(n):
        s = words[i]
        S[i][:len(s)] = map(ord, s)
    
    # Initialize the memoization table
    memo = [[[[-1] * (L + 2) for _ in range(M + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Base cases for memoization table
    for i in range(n + 1):
        for p in range(M + 1):
            for c in range(L + 2):
                memo[i][i][p][c] = 1
    
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            for p in range(M + 1):
                memo[i][j][p][L + 1] = 0
            for c in range(L + 2):
                memo[i][j][M][c] = i + 1 == j
    
    # Depth-first search function to fill the memoization table
    def dfs(l, r, p, c):
        if memo[l][r][p][c] != -1:
            return memo[l][r][p][c]
        res = dfs(l, r, p, c + 1)
        for i in range(l + 1, r + 1):
            if S[i - 1][p] != ca + c - 1 if S[i - 1][p] != cq else c == 0:
                break
            res += dfs(l, i, p + 1, 0) * dfs(i, r, p, c + 1) % MOD
        memo[l][r][p][c] = res = res % MOD
        return res
    
    # Return the result of the dfs function
    return dfs(0, n, 0, 0)