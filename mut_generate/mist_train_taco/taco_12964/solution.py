"""
QUESTION:
For a positive integer n, we denote the integer obtained by reversing the decimal notation of n (without leading zeroes) by rev(n). For example, rev(123) = 321 and rev(4000) = 4.

You are given a positive integer D. How many positive integers N satisfy rev(N) = N + D?

Constraints

* D is an integer.
* 1 ≤ D < 10^9

Input

Input is given from Standard Input in the following format:


D


Output

Print the number of the positive integers N such that rev(N) = N + D.

Examples

Input

63


Output

2


Input

75


Output

0


Input

864197532


Output

1920
"""

def count_reversible_numbers(D: int) -> int:
    def solve(d: int, K: int) -> int:
        r = 1
        for k in range(K, 1, -2):
            if d >= 10 ** k:
                return 0
            t = -d % 10
            d = abs((d - t * (10 ** (k - 1) - 1)) // 10)
            r *= 10 - t - (K == k)
        return r * 10 ** (K % 2) if d == 0 else 0
    
    result = 0
    l = len(str(D))
    for k in range(l, 2 * l + 1):
        result += solve(D, k)
    return result