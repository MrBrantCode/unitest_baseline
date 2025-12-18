"""
QUESTION:
Implement a function `enhanced_fibfib(n: int)` that calculates the nth term of a series where `fibfib(0) == 0`, `fibfib(1) == 0`, `fibfib(2) == 1`, `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) + fibfib(n-4)` for `n < 1000`, and `fibfib(n) == 2 * fibfib(n-1000)` for `n >= 1000`. The input `n` is guaranteed to be in the range `0 <= n <= 10^6`.
"""

def enhanced_fibfib(n: int) -> int:
    limit = 10**6
    mod = 10**9+7
    fibfib_series = [0]*max(n+1,limit+1) 
    fibfib_series[2] = 1

    if (n <= 2):
        return fibfib_series[n]
    else: 
        for i in range(3, n+1):
            if i < 1000:
                fibfib_series[i] = (fibfib_series[i-1] + fibfib_series[i-2] + fibfib_series[i-3] + fibfib_series[i-4]) % mod
            elif i >= 1000:
                fibfib_series[i] = (fibfib_series[i-1000] * 2) % mod
                
        return fibfib_series[n]