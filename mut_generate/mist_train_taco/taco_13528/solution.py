"""
QUESTION:
Chef wants to select a subset $S$ of the set $\{1, 2, \ldots, N\}$ such that there are no two integers $x, y \in S$ which satisfy $\frac{x}{y} = M$.
Help Chef find the maximum size of a subset $S$ he can choose and the number of ways in which he can choose a subset $S$ with this maximum size. Since the number of ways to choose $S$ can be very large, calculate it modulo $998,244,353$.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $M$.

-----Output-----
For each test case, print a single line containing two space-separated integers ― the maximum size of a subset Chef can choose and the number of ways to choose a subset with this maximum size modulo $998,244,353$. Note that only the number of ways to choose a subset should be printed modulo $998,244,353$.

-----Constraints-----
- $1 \le T \le 10,000$
- $2 \le M \le N \le 10^{18}$

-----Example Input-----
3
5 2
10 2
100 3

-----Example Output-----
4 1
6 12
76 49152

-----Explanation-----
Example case 1: The only subset $S$ with the maximum size which Chef can choose is $\{1, 3, 4, 5\}$.
"""

def max_subset_size_and_ways(N, M):
    MOD = 998244353
    
    def groupsInInterval(L, R, M, N):
        if R <= N:
            return R - (L - 1) - (R // M - (L - 1) // M)
        else:
            return 0
    
    def power(a, b):
        res = 1
        while b > 0:
            if b % 2:
                res *= a
                res %= MOD
            b //= 2
            a *= a
            a %= MOD
        return res
    
    taken, ways = 0, 1
    for i in range(1, 70):
        L = N // M ** i + 1
        R = N // M ** (i - 1)
        groups = groupsInInterval(L, R, M, N)
        if i % 2 == 0:
            taken += i // 2 * groups
            ways *= power(i // 2 + 1, groups)
        else:
            taken += (i + 1) // 2 * groups
            ways *= 1
    
    return taken, ways % MOD