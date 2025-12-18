"""
QUESTION:
Find the number of integers between 1 and K (inclusive) satisfying the following condition, modulo 10^9 + 7:

* The sum of the digits in base ten is a multiple of D.

Constraints

* All values in input are integers.
* 1 \leq K < 10^{10000}
* 1 \leq D \leq 100

Input

Input is given from Standard Input in the following format:


K
D


Output

Print the number of integers satisfying the condition, modulo 10^9 + 7.

Examples

Input

30
4


Output

6


Input

1000000009
1


Output

2


Input

98765432109876543210
58


Output

635270834
"""

def count_integers_with_digit_sum_multiple(K: str, D: int) -> int:
    MOD = 10**9 + 7
    S = list(map(int, K))
    N = len(S)
    
    # Initialize 2D lists for dynamic programming
    dp0 = [[0] * D for _ in range(N + 1)]
    dp1 = [[0] * D for _ in range(N + 1)]
    
    dp0[0][0] = 1
    
    for i, a in enumerate(S):
        for j in range(D):
            if not dp0[i][j] and not dp1[i][j]:
                continue
            for k in range(10):
                if k < a:
                    dp1[i + 1][(j + k) % D] += dp0[i][j]
                    dp1[i + 1][(j + k) % D] += dp1[i][j]
                elif k == a:
                    dp0[i + 1][(j + k) % D] += dp0[i][j]
                    dp1[i + 1][(j + k) % D] += dp1[i][j]
                else:
                    dp1[i + 1][(j + k) % D] += dp1[i][j]
                dp0[i + 1][(j + k) % D] %= MOD
                dp1[i + 1][(j + k) % D] %= MOD
    
    ans = (dp0[N][0] + dp1[N][0] - 1) % MOD
    return ans