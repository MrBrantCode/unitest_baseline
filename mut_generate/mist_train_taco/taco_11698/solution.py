"""
QUESTION:
Link to Russian translation of problem

You are given positive integer N. How many unordered pairs of integers from 1 to N are coprime?

Input
The first line contains one integer T denoting the number of test cases.
The following T lines contain one number each - N and describe each test case.

Output
For each test case output one integer per line - answer for the question.

Constraints
N ≤ 10^7
T ≤ 10

SAMPLE INPUT
2
3
4

SAMPLE OUTPUT
4
6
"""

def count_coprime_pairs(N):
    M = {}
    
    def f(n):
        if n in M:
            return M[n]
        c = n * n
        i = n
        while i > 1:
            z = n // i
            j = n // (z + 1)
            c -= f(z) * (i - j)
            i = j
        M[n] = c
        return c
    
    return (f(N) + 1) // 2