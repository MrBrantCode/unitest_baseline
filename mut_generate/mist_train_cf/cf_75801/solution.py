"""
QUESTION:
Given an array of integers A, calculate the sum of the widths of all subsequences of A, where the width of a subsequence is the difference between the maximum and minimum element. Return the result modulo 10^9 + 7. The length of A is between 1 and 20000 (inclusive), and each element of A is between 1 and 20000 (inclusive). Implement a function sumSubseqWidths(A) to solve the problem.
"""

def sumSubseqWidths(A):
    MOD = 10**9 + 7
    N = len(A)
    pow2 = [1] * N
    for i in range(1, N):
        pow2[i] = pow2[i - 1] * 2 % MOD
    
    A.sort()
    res = 0
    for i, a in enumerate(A):
        res = (res + a * (pow2[i] - pow2[N - i - 1])) % MOD
    return res