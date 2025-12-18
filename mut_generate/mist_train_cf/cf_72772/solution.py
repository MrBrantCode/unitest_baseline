"""
QUESTION:
Write a function named `countArrangement` that determines the total count of beautiful arrangements that can be formulated given an integer `n`, where a beautiful arrangement is a permutation of `n` integers (1-indexed) such that for every `i` (`1 &lt;= i &lt;= n`), either `perm[i]` is a multiple of `i` or `i` is a multiple of `perm[i]`. The input `n` is restricted to `1 &lt;= n &lt;= 15`.
"""

def countArrangement(n: int) -> int:
    def calculate(num, X):
        if len(X) == 1: return 1
        total = 0
        for i in range(len(X)):
            if X[i] % num == 0 or num % X[i] == 0:
                total += calculate(num - 1, X[:i] + X[i+1:])
        return total
    return calculate(n, tuple(range(1, n + 1)))