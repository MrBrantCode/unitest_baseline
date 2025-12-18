"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a given integer `n` where `n` can be as large as 1000. The function should optimize execution time and avoid potential stack overflow issues due to Python's native recursion limit.
"""

def entance(n):
    fac_table = [0]*(n+1)
    fac_table[0] = 1
    for i in range(1, n+1):
        fac_table[i] = i * fac_table[i-1]
    return fac_table[n]