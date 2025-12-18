"""
QUESTION:
John Doe has an n × m table. John Doe can paint points in some table cells, not more than one point in one table cell. John Doe wants to use such operations to make each square subtable of size n × n have exactly k points.

John Doe wondered, how many distinct ways to fill the table with points are there, provided that the condition must hold. As this number can be rather large, John Doe asks to find its remainder after dividing by 1000000007 (109 + 7).

You should assume that John always paints a point exactly in the center of some cell. Two ways to fill a table are considered distinct, if there exists a table cell, that has a point in one way and doesn't have it in the other.

Input

A single line contains space-separated integers n, m, k (1 ≤ n ≤ 100; n ≤ m ≤ 1018; 0 ≤ k ≤ n2) — the number of rows of the table, the number of columns of the table and the number of points each square must contain.

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier. 

Output

In a single line print a single integer — the remainder from dividing the described number of ways by 1000000007 (109 + 7).

Examples

Input

5 6 1


Output

45

Note

Let's consider the first test case: 

<image> The gray area belongs to both 5 × 5 squares. So, if it has one point, then there shouldn't be points in any other place. If one of the white areas has a point, then the other one also must have a point. Thus, there are about 20 variants, where the point lies in the gray area and 25 variants, where each of the white areas contains a point. Overall there are 45 variants.
"""

def count_distinct_ways(n, m, k):
    M = 1000000007
    N = n * n
    
    # Precompute modular inverses
    iv = [0] * (N + 1)
    iv[1] = 1
    for i in range(2, N + 1):
        iv[i] = M - M // i * iv[M % i] % M
    
    # Precompute factorials and their modular inverses
    f1 = [1] * (N + 1)
    for i in range(1, N + 1):
        f1[i] = f1[i - 1] * i % M
    
    f2 = [1] * (N + 1)
    for i in range(1, N + 1):
        f2[i] = f2[i - 1] * iv[i] % M
    
    left = m % n
    
    # Helper function for modular exponentiation
    def powM(b, p):
        r = 1
        while p > 0:
            if p % 2 > 0:
                r = r * b % M
            b = b * b % M
            p //= 2
        return r
    
    # Precompute combinations
    c = [[powM(f1[n] * f2[j] % M * f2[n - j] % M, m // n + i) for j in range(n + 1)] for i in range(2)]
    
    # Dynamic programming table
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(k + 1):
            if j > i * n or j < k - (n - i) * n:
                continue
            for l in range(min(n, k - j) + 1):
                dp[i + 1][j + l] = (dp[i + 1][j + l] + c[i < left][l] * dp[i][j]) % M
    
    return dp[n][k]