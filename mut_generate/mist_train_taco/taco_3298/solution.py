"""
QUESTION:
Snuke loves permutations. He is making a permutation of length N.

Since he hates the integer K, his permutation will satisfy the following:

* Let the permutation be a_1, a_2, ..., a_N. For each i = 1,2,...,N, |a_i - i| \neq K.



Among the N! permutations of length N, how many satisfies this condition?

Since the answer may be extremely large, find the answer modulo 924844033(prime).

Constraints

* 2 ≦ N ≦ 2000
* 1 ≦ K ≦ N-1

Input

The input is given from Standard Input in the following format:


N K


Output

Print the answer modulo 924844033.

Examples

Input

3 1


Output

2


Input

4 1


Output

5


Input

4 2


Output

9


Input

4 3


Output

14


Input

425 48


Output

756765083
"""

def count_valid_permutations(n, k):
    mod = 924844033
    
    # Precompute factorials modulo mod
    fac = [1] * (n + 1)
    for j in range(1, n + 1):
        fac[j] = fac[j - 1] * j % mod
    
    # Initialize DP table
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1
    
    # Fill DP table
    for i in range(min(n, 2 * k)):
        idx = i
        while idx < n:
            ndp = [[0] * 2 for _ in range(n + 1)]
            if idx == i:
                for ll in range(n + 1):
                    dp[ll][0] += dp[ll][1]
                    dp[ll][1] = 0
            for l in range(1, n + 1):
                ndp[l][0] = sum(dp[l])
                if idx - k >= 0:
                    ndp[l][0] += dp[l - 1][0]
                if idx + k < n:
                    ndp[l][1] = sum(dp[l - 1])
                ndp[l][0] %= mod
            ndp[0][0] = 1
            dp = ndp
            idx += 2 * k
    
    # Compute the final answer
    ans = fac[n]
    for m in range(1, n + 1):
        if m % 2:
            ans -= sum(dp[m]) * fac[n - m] % mod
        else:
            ans += sum(dp[m]) * fac[n - m] % mod
        ans %= mod
    
    return ans