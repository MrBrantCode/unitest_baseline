"""
QUESTION:
Given a positive integer `n` where `1 <= n <= 2*10^9`, find the minimum number of days to eat `n` oranges. Each day, you can eat one orange, `n/2` oranges if `n` is divisible by 2, `2*(n/3)` oranges if `n` is divisible by 3, or `3*(n/5)` oranges if `n` is divisible by 5. Only one action can be chosen per day. Write a function `minDays(n)` to return the minimum number of days required.
"""

import functools

def minDays(n: int) -> int:
    @functools.lru_cache(None)
    def dp(n):
        if n == 0: return 0
        return min(n % 2 + 1 + dp(n // 2), n % 3 + 1 + dp(n // 3), 1 + dp(n - 1), n % 5 + 1 + dp(n // 5))

    return dp(n)