"""
QUESTION:
There are N people, conveniently numbered 1 through N.
We want to divide them into some number of groups, under the following two conditions:
 - Every group contains between A and B people, inclusive.
 - Let F_i be the number of the groups containing exactly i people. Then, for all i, either F_i=0 or C≤F_i≤D holds.
Find the number of these ways to divide the people into groups.
Here, two ways to divide them into groups is considered different if and only if there exists two people such that they belong to the same group in exactly one of the two ways.
Since the number of these ways can be extremely large, print the count modulo 10^9+7.

-----Constraints-----
 - 1≤N≤10^3
 - 1≤A≤B≤N
 - 1≤C≤D≤N

-----Input-----
The input is given from Standard Input in the following format:
N A B C D

-----Output-----
Print the number of ways to divide the people into groups under the conditions, modulo 10^9+7.

-----Sample Input-----
3 1 3 1 2

-----Sample Output-----
4

There are four ways to divide the people:
 - (1,2),(3)
 - (1,3),(2)
 - (2,3),(1)
 - (1,2,3)
The following way to divide the people does not count: (1),(2),(3). This is because it only satisfies the first condition and not the second.
"""

def count_group_divisions(N, A, B, C, D):
    mod = 10 ** 9 + 7
    
    # Precompute factorials and their modular inverses
    factorials = [1] * (N + 1)
    for i in range(2, N + 1):
        factorials[i] = factorials[i - 1] * i % mod
    
    def inv(x):
        ret = 1
        k = mod - 2
        y = x
        while k:
            if k & 1:
                ret = ret * y % mod
            y = y * y % mod
            k //= 2
        return ret
    
    finv = [0] * (N + 1)
    finv[N] = inv(factorials[N])
    for i in range(N - 1, 0, -1):
        finv[i] = finv[i + 1] * (i + 1) % mod
    
    def calc(i, j, k):
        tmp = finv[N - j]
        tmp = tmp * finv[k] % mod
        tmp = tmp * factorials[N - j + i * k] % mod
        y = finv[i]
        ret = 1
        while k:
            if k & 1:
                ret = ret * y % mod
            y = y * y % mod
            k //= 2
        return ret * tmp % mod
    
    dp = [[0] * (N + 1) for _ in range(B + 1)]
    for i in range(B + 1):
        dp[i][0] = 1
    
    ls = [0] + list(range(C, D + 1))
    l = len(ls)
    
    for i in range(A, B + 1):
        for j in range(1, N + 1):
            tmp = 0
            for k in ls:
                if k > j / i:
                    break
                tmp = (tmp + dp[i - 1][j - i * k] * calc(i, j, k)) % mod
            dp[i][j] = tmp
    
    return dp[B][N]