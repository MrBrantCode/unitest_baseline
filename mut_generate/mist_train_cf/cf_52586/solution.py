"""
QUESTION:
Implement the `complex_fibber` function, which calculates the n-th number in a complex series. The function takes four parameters: n, m, p, and q, where m > 2, p < m, and q < p. The series is defined as:
- complex_fibber(0,m,p,q) == 0
- complex_fibber(1,m,p,q) == 0
- complex_fibber(2,m,p,q) == 1
- complex_fibber(n,m,p,q) == complex_fibber(n-1,m,p,q) + complex_fibber(n-2,m,p,q) + complex_fibber(n-3,m,p,q) - complex_fibber(n-m,p,q) + 3*complex_fibber(n-p,p,q) - 2*complex_fibber(n-q,q) for m <= n.
Implement the function using dynamic programming for efficient computation, assuming that for negative indices, the series' value is 0.
"""

def complex_fibber(n: int, m: int, p: int, q: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    dp = [0] * (n+1)
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + (dp[i-3] if i>=3 else 0) - (dp[i-m] if i>=m else 0) + 3*(dp[i-p] if i>=p else 0) - 2*(dp[i-q] if i>=q else 0)
    
    return dp[n]