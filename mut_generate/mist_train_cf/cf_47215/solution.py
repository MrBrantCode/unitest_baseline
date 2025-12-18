"""
QUESTION:
Given a non-negative integer `n` (0 ≤ `n` ≤ 37), calculate the value of the `n`-th number in the Tribonacci sequence, where `T0` is 0, `T1` and `T2` are both 1, and for any `n` ≥ 0, `Tn+3` is the sum of `Tn`, `Tn+1`, and `Tn+2`. The result should be within the range of a 32-bit integer (i.e., `result` ≤ `2^31 - 1`). Implement a function `tribonacci(n)` to solve this problem.
"""

def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    trib = [0, 1, 1] + [0] * (n - 2)

    for i in range(3, n + 1):
        trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]

    return trib[n]